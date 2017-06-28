#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <ctype.h>

// ��תdata[start...end-1]
void reverse_data( char *data, int start, int end  )
{
    char temp = '0';

    assert( data != NULL && start < end );
    while ( start < end )
    {
        temp = data[start];
        data[start] = data[--end];
        data[end] = temp;
        ++start;
    }
}

/**< �ж���������ֵ�ĺϷ��ԣ��Լ��ǿո��ַ�����ʼλ�á�
 *  1. �Ƿ������ȷ�������ţ�����"+123", "-123"��
 *  2. �ַ������ַ��Ƿ���������ַ���
 *  3. �ַ�����ʼ���ַ���ո��ǺϷ��ģ����磬��  +123����
 *  4. ֻ��һ��'.'���
 **< ����:
 * @data: ��ʾ�����ַ�;
 * @nonspace_index:�ǿո����
 **< ����ֵ���������ǺϷ���ֵ���򷵻�1�����򷵻�0��
 */
int check_logic( const char *data, int *nonspace_index )
{
    int flag = 1;
    int start = 0;
    int point_cnt = 0;

    assert( data != NULL );
    /* PS. if data is not space(' ', '\n'), isspace() return 0. */
    for ( ; isspace( data[start] )!= 0
            && data[start] != '\0'; ++start );

    // �ж������Ƿ�Ϊ����
    *nonspace_index = start;
    if ( data[start] == '-' || data[start] == '+' )
    {
        ++start;
    }

    /* PS. if ch is digit character, isdigit() return 1; otherwise return 0. */
    for ( ; data[start] != '\0'; ++start )
    {
        if ( isdigit( data[start] ) || data[start] == '.' )
        {
            // �ж�����ΪС���ĸ�ʽ�Ƿ���ȷ��
            if ( data[start] == '.' && point_cnt == 0 )
            {
                ++point_cnt;
            }
            else if ( point_cnt > 1 )
            {
                break;
            }
        }
    }

    // ��С������������ݣ��򲻺Ϸ�
    if ( data[start] != '\0' )
    {
        flag = 0;
    }

    return flag;
}

/**< notice: ���뵽�ú����������Ѿ�����ת�����ֵ�����������Ϊ��λ�����ұ�Ϊ���λ
 **< return: ������ݵĳ��ȡ�
 */
int compute_value( const char *lhs, int lhs_start_index,
                   const char *rhs, int rhs_start_index,
                   char *result )
{
    int i = 0, j = 0, res_i = 0;
    int tmp_i = 0;
    int carry = 0;

    for ( i = lhs_start_index; lhs[i] != '\0'; ++i, ++tmp_i )
    {
        res_i = tmp_i;
        carry = 0;

        for ( j = rhs_start_index; rhs[j] != '\0'; ++j )
        {
            int tmp_lhs = lhs[i] - '0';
            int tmp_rhs = rhs[j] - '0';
            carry += ( result[res_i] - '0' );
            carry += ( tmp_lhs * tmp_rhs );
            result[res_i++] = ( carry % 10 + '0' );
            carry /= 10;
        }

        while ( carry )
        {
            result[res_i++] = ( carry % 10 + '0' );
            carry /= 10;
        }
    }
    result[res_i] = '\0';

    return res_i;
}

int has_point( char *data, int index, int *point_index )
{
    int start = index;

    for ( ; data[start] != '\0'; ++start )
    {
        if ( data[start] == '.' )
        {
            *point_index = start;
            break;
        }
    }

    return ( data[start] != '\0' );
}

int is_neg( char *data, int *index )
{
    int flag = 0;
    int start = *index;
    if ( data[start] == '-' || data[start] == '+' )
    {
        if ( data[start] == '-' )
            flag = 1;
        ++start;
    }

    *index = start;
    return flag;
}

void copy_c( char * dest, const char *src )
{
    while ( *src != '\0' )
    {
        if ( *src != '.' )
            *dest++ = *src;
        src++;
    }
}

int compute_decimals( char *lhs, int lhs_point_index,
                      char *rhs, int rhs_point_index,
                      char *result  )
{
    int lhs_length = strlen( lhs );
    int rhs_length = strlen( rhs );
    int result_point_index = lhs_length + rhs_length;
    int result_length = 0, i = 0;
    char *tmp_lhs = NULL;
    char *tmp_rhs = NULL;

    // �����ڽ���з���С�����λ�ã����ݵ�������С�����ֳ���֮��
    // ���磬rhs = "12.345", lhs = "3.45", result = "xxx.xxxxx"
    result_point_index -= ( lhs_point_index + rhs_point_index );

    // ���䲢����
    if ( lhs_point_index )
    {
        tmp_lhs = (char *)malloc( sizeof(char) * lhs_length );
        assert( tmp_lhs != NULL );
        copy_c( tmp_lhs, lhs );
        tmp_lhs[lhs_length - 1] = '\0';
    }
    else
    {
        tmp_lhs = lhs;
    }

    if ( rhs_point_index )
    {
        tmp_rhs = (char *)malloc( sizeof(char) * rhs_length );
        assert( tmp_rhs != NULL );
        copy_c( tmp_rhs, rhs );
        tmp_rhs[rhs_length - 1] = '\0';
    }
    else
    {
        tmp_rhs = rhs;
    }

    // tmp_lhs��lhs��һ��С����
    reverse_data( tmp_lhs, 0, lhs_length - 1 );
    reverse_data( tmp_rhs, 0, rhs_length - 1 );
    result_length = compute_value( tmp_lhs, 0, tmp_rhs, 0, result );
    for ( i = result_length; i > result_point_index; --i )
    {
        result[i] = result[i - 1];
    }

    result[result_point_index] = '.';
    ++result_length;
    result[result_length] = '\0';

    // �ͷ���Դ
    if ( lhs_point_index )
    {
        free( tmp_lhs ), tmp_lhs = NULL;
    }

    if ( rhs_point_index )
    {
        free( tmp_rhs ), tmp_rhs = NULL;
    }

    return result_length;
}

// ���ؽ����ֵ�ĳ���
int big_number_multiply( char *lhs, char *rhs, char *result )
{
    int lhs_start_index = 0, lhs_point_index = 0;
    int rhs_start_index = 0, rhs_point_index = 0;
    int result_is_neg = 0;
    int result_length = 0;

    assert( lhs != NULL && rhs != NULL && result != NULL );
    // ������ݵĺϷ���
    if ( !(check_logic( lhs, &lhs_start_index )
            && check_logic( rhs, &rhs_start_index )) )
    {
        return -1;
    }

    // ��������Ƿ�Ϊ����
    result_is_neg = is_neg( lhs, &lhs_start_index );
    if ( is_neg( rhs, &rhs_start_index) )
    {
        result_is_neg = result_is_neg == 1 ?  0 : 1;
    }

    // ����Ƿ�������ֵ�д���һ��С�������߶���С��
    if ( !( has_point( lhs, lhs_start_index, &lhs_point_index )
            && has_point( rhs, rhs_start_index, &rhs_point_index ) ) )
    {
        reverse_data( lhs, lhs_start_index, strlen(lhs) );
        reverse_data( rhs, rhs_start_index, strlen(rhs) );
        result_length = compute_value( lhs, lhs_start_index,
                                       rhs, rhs_start_index, result );
        reverse_data( lhs, lhs_start_index, strlen(lhs) );
        reverse_data( rhs, rhs_start_index, strlen(rhs) );
    }
    else // һ����ֵ����С������
    {
        result_length = compute_decimals(
                          lhs + lhs_start_index, lhs_point_index - lhs_start_index + 1,
                          rhs + rhs_start_index, rhs_point_index - rhs_start_index + 1,
                          result );
    }
    if ( result_is_neg )
        result[result_length++] = '-';
    reverse_data( result, 0, result_length );
    result[result_length] = '\0';

    return result_length;
}

int main()
{
    char lhs[] = "-1.235";
    char rhs[] = "    3.456";
    char result[40];

    memset( result, '0', sizeof(result) );

    big_number_multiply( lhs, rhs, result );
    printf( "%s\n", result );
    return 0;
}
