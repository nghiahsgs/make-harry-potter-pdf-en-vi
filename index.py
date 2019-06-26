import utils
import io

list_paras_en=utils.get_list_paragraph_en("https://www.bookscool.com/en/Harry-Potter-and-the-Philosophers-Stone/1")

f = io.open("list_paras_en.txt", 'a', encoding='utf-8')
for para_en in list_paras_en:
    f.write(para_en)
    f.write('\n')
f.close()

# list_paras_vi = utils.get_list_paragraph_vi("https://gacsach.com/doc-truc-tuyen/8144/harry-potter-va-hon-da-phu-thuy-chuong-01.html")
# f = io.open("list_paras_vi.txt", 'a', encoding='utf-8')
# for para_vi in list_paras_vi:
#     f.write(para_vi)
#     f.write('\n')
# f.close()



