package main.model;

import javax.persistence.*;

import java.io.Serializable;




/**
 * Created by youye on 17-6-17.
 *
 * 小技巧:通过hibernate来进行插入操作的时候，
 * 不管是一对多、一对一还是多对多，都只需要记住一点，
 * 在哪个实体类声明了外键，就由哪个类来维护关系，在保存数据时，
 * 总是先保存的是没有维护关联关系的那一方的数据，后保存维护了关联关系的那一方的数据
 */

@Entity
@Table(name="user_table")
public class User implements Serializable {
    private Integer UserId;
    private String UserNick;
    private String UserPasswd;
    //0 不是 1 是
    private int isAdmin;


    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "user_id", length = 30)
    public Integer getUserId() {
        return UserId;
    }

    public void setUserId(Integer userId) {
        UserId = userId;
    }

    @Column(name = "user_nick", length = 30)
    public String getUserNick() {
        return UserNick;
    }

    public void setUserNick(String userNick) {
        UserNick = userNick;
    }

    @Column(name = "user_password", length = 30)
    public String getUserPasswd() {
        return UserPasswd;
    }

    public void setUserPasswd(String userPasswd) {
        UserPasswd = userPasswd;
    }

    @Column(name = "user_is_admin",length = 2)
    public int getIsAdmin() {
        return isAdmin;
    }

    public void setIsAdmin(int isAdmin) {
        this.isAdmin = isAdmin;
    }
}
