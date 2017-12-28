# coding=utf-8
import pandas as pd
import requests
from lxml import etree
from io import BytesIO


def extract_table_to_list(url,refer_table_id=None,decodeing="utf-8"):
    '''
    提取html中的table转化为列表
    :param url: url地址
    :param refer_table_id: 包含一个table的元素的id
    :param decodeing: 网页解码方式
    :return: list，list中每天数据是一个字典
    '''
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}
    response = requests.get(url,headers=headers)
    html = etree.HTML(response.content.decode(decodeing))
    content = html.xpath("//div[@id='{}']".format(refer_table_id))
    if not content or len(content)>1:
        raise  ValueError("xpath error")
    fp = BytesIO(etree.tostring(content[0]))
    df_list = pd.read_html(fp)
    if not df_list or len(df_list)>1:
        raise  ValueError("NO table exist or not only one table")
    df = df_list[0]
    df.columns = df.iloc[0, :]
    new_df = df.iloc[1:,:]  #DataFrame
    ret = new_df.to_dict(orient='records')
    return ret

if __name__ == '__main__':
    url = "http://www.shxda.gov.cn/structure/ztzl/xzcfxxgs/xxgs/zw_27842_1.htm"
    url2 = "http://www.shxda.gov.cn/structure/ztzl/xzcfxxgs/xxgs/zw_30599_1.htm"
    ret = extract_table_to_list(url2,refer_table_id="content")
    print(ret)

