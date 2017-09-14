#-*-coding: utf-8-*-
import xml.etree.ElementTree as et
import json


def hexstr2str(content):
    ret = ""
    for idx in xrange(0, len(content)-1, 2):
        try:
            val = int(content[idx] + content[idx+1], base=16)
            if(val != 0):
                ret += chr(val)
        except ValueError:
            print("This is Wrong!!!!!!!!!!!!!!!!!!!!!!!!!!111" + content[idx] + content[idx+1])
    return ret


def process_file(f):
    xml_file_text = f.read().decode('gb2312').encode('utf-8').replace('gb2312', 'utf-8')
    root = et.fromstring(xml_file_text)
    for inst in root.find("MessageFlow").findall("NetInterInst"):
        for msg in inst.findall("Message"):
            msg_content = "<?xml version=\"1.0\"?>\n" + hexstr2str(msg.text).strip()
            if(msg_content.find("request") == -1):
                continue
            json_str  = et.fromstring(msg_content).find("content").attrib["value"]
            req_name = json.loads(json_str).keys()[0]
            inst.attrib["SimpleDesp"] = req_name
            #json_req = json.load(et.fromstring(msg_content).find("content").attrib["value"])

    new_f = open("ttt.fcas", "wb")
    new_f.write(et.tostring(root, 'gb2312'))
    new_f.close()






def main():
    #file_name = raw_input("please input the file path:")
    f = open('C:/Users/10129693/Desktop/test1.fcas', "rb")
    process_file(f)





if __name__ == '__main__':
    main()


