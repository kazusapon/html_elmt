from html.parser import HTMLParser

class HTMLAnalysis(HTMLParser):
    def __init__(self):
        super().__init__()
        #HTMLのCLass等と設定値を格納するリスト
        self.attr_ary = []
        #HTMLのタグとClass、IDのセットを格納するディクショナリ
        self.tags_dic = {}

    def handle_starttag(self, tag, attrs):
        if tag not in self.tags_dic:
            self.tags_dic[tag] = ''
        
        for attr in attrs:
            self.attr_ary.append(list(attr))
            self.attr_ary = self.attr_ary[0]
        
        if len(self.attr_ary) >= 1:
            if tag not in self.tags_dic:
                self.tags_dic[tag] = self.attr_ary
            else:
                tmp = []
                tmp = list(self.tags_dic[tag])
                tmp.append(self.attr_ary)
                self.tags_dic[tag] = tmp
        
        self.reset_attrs()

    def reset_attrs(self):
        self.attr_ary = []
        return self.attr_ary


def html_list(file):
    parser = HTMLAnalysis()
    parser.feed(file)
    return parser.tags_dic

def check_class(file, class_name):
    parser = HTMLAnalysis()
    parser.feed(file)
    elm_val = []
    html_elm = parser.tags_dic
    for elm in html_elm.values():
        if elm != "":
            elm_val = elm_val + elm
        
    for val in elm_val:
        if val[1] == class_name:
            return True
    
    return False
