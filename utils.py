import io
import requests
import bs4
def writeFile(filePath,ndungFile):
    f = io.open(filePath, 'w', encoding='utf-8')
    f.write(ndungFile)
    f.close()
def get_list_paragraph_vi(linkChap):
    #"https://gacsach.com/doc-truc-tuyen/8144/harry-potter-va-hon-da-phu-thuy-chuong-01.html"
    
    kq_vi = requests.get(linkChap)
    # print(linkChap)
    # print(kq_vi.status_code)
    dom_vi = bs4.BeautifulSoup(kq_vi.text)


    list_result=[]
    eles = dom_vi.select('.story_text')

    for ele in eles:
        list_result.append(ele.getText())
    
    return list_result


def get_list_paragraph_en(linkChap):
    #"https://www.bookscool.com/en/Harry-Potter-and-the-Philosophers-Stone/1"
    kq_en = requests.get(linkChap)
    # print(linkChap)
    # print(kq_en.status_code)
    dom_en = bs4.BeautifulSoup(kq_en.text)
    ele = dom_en.select('#content-text')[0]
    
    paras = ele.getText().split('   ')
    list_result = []
    for para in paras:
        para = para.strip()
        if para:
            list_result.append(para)
    
    return list_result

        
    
    


