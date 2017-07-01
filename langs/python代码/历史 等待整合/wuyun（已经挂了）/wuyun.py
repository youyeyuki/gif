from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(open('wuyun', 'r', encoding='utf-8'), "html.parser")
# print(soup.tbody.contents[1])





# for child in soup.tbody.children:
#     print(child)


# for child in soup.tbody.descendants:
#     print (child)

#
# tag_tbody = soup.tbody
#
# for child in tag_tbody.children:
#     s = BeautifulSoup(str(child), "html.parser")
#     ls = s.find_all('td')
#     if not ls:
#         pass
#     else:
#         date = re.findall("<td [^>]+>(.*)</td>", str(ls[0]))
#         company = re.findall("<td [^>]+><a [^>]+>(.*)</a></td>", str(ls[1]))
#         web = re.findall("<td [^>]+><a [^>]+>(.*)</a></td>", str(ls[2]))
#         print(date, company, web)
import re
s ="""<tr>
<th>2016-03-18</th>
<td><a href="/bugs/wooyun-2016-0186368">看我如何漫游豆瓣内网</a>
<img alt="" class="credit" src="/images/credit.png">
</img></td>
<th><a href="/bugs/wooyun-2016-0186368#comment" title="评论一下">38/149</a></th>
<th><a href="/whitehats/if、so" title="if、so">if、so</a></th>
</tr>"""


title = re.findall("<td><a [^>]+>(.*)</a>\s+</td>", s)[0]
print(title)


        # for i in range(0,len(tag_tbody.contents)):
        #     print(tag_tbody.contents[i])
