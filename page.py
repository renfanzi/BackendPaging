class Pagination:
    """
    explain:
        obj = Pagination(1, 20, 1001)
        print(obj.start)
        print(obj.end)
        obj.item_pages --> 求分页的页码
    all_item :need the query library to count
    """
    """
    all_item: 总count
    current_page: 你的页数、
    appear_page： 每页多少条数据
    """

    def __init__(self, all_item, current_page=0, appear_page=50):
        try:
            self.appear_page = appear_page
            self.int = int(current_page)
            self.all_item = all_item
            page = self.int
        except:
            self.all_item = 0
            page = 1
        if page < 1:
            page = 1

        all_pager, c = divmod(all_item, self.appear_page)
        if c > 0:
            all_pager += 1

        self.current_page = page
        self.all_pager = all_pager

    @property
    def start(self):
        return (self.current_page - 1) * self.appear_page

    @property
    def end(self):
        return self.current_page * self.appear_page

    @property
    def item_pages(self):
        all_pager, c = divmod(self.all_item, self.appear_page)
        if c > 0:
            all_pager += 1
        return 0, all_pager

    def string_pager(self, base_url="/index/"):
        list_page = []
        if self.all_pager < 11:
            s = 1
            t = self.all_pager + 1
        else:  # 总页数大于11
            if self.current_page < 6:
                s = 1
                t = 12
            else:
                if (self.current_page + 5) < self.all_pager:
                    s = self.current_page - 5
                    t = self.current_page + 5 + 1
                else:
                    s = self.all_pager - 11
                    t = self.all_pager + 1

        if self.current_page == 1:
            prev = '<a href="javascript:void(0);">上一页</a>'
        else:
            prev = '<a href="%s%s">上一页</a>' % (base_url, self.current_page - 1,)
        list_page.append(prev)

        for p in range(s, t):  # 1-11
            if p == self.current_page:
                temp = '<a class="active" href="%s%s">%s</a>' % (base_url, p, p)
            else:
                temp = '<a href="%s%s">%s</a>' % (base_url, p, p)
            list_page.append(temp)
        if self.current_page == self.all_pager:
            nex = '<a href="javascript:void(0);">下一页</a>'
        else:
            nex = '<a href="%s%s">下一页</a>' % (base_url, self.current_page + 1,)

        list_page.append(nex)

        str_page = "".join(list_page)

        return str_page


if __name__ == '__main__':
    obj = Pagination(1001, 6, 100)
    print(obj.start)
    print(obj.end)
    print(obj.item_pages)
