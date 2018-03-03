# -*-coding:utf-8-*-
import os,sys,time,random
import requests,json
from item import _Item
import logging

print('\n\n\n%s\t%5s\t'%('\t'*2,'爬虫程序正在运行！'))
print('\n\n\t%s'%('*'*57))
print('\t*\t%5s\t%s*'%('请不要关闭当前对话，如需关闭。','\t'*2))
print('\t*\t%5s\t*'%('请用Ctrl+C使数据完整保存后，再关闭对话框。'))
print('\t*\t%5s\t*'%('请用Ctrl+C使数据完整保存后，再关闭对话框。'))
print('\t*\t%5s\t%s*'%('请不要关闭当前对话，如需关闭。','\t'*2))
print('\t%s'%('*'*57))


logging.basicConfig(filename = 'log/info.log', format = '%(asctime)s - %(levelname)s - %(message)s', level = logging.INFO)

class Snake(object):

    def __init__(self):
        super(Snake, self).__init__()

        logging.info("Start")

        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3226.400 QQBrowser/9.6.11681.400",
            "DNT": "1",
            "Host": "www.lagou.com",
            "Origin": "https://www.lagou.com",
            "Referer": "https://www.lagou.com/jobs/list_",
            "X-Anit-Forge-Code": "0",
            "X-Anit-Forge-Token": None,
            "X-Requested-With": "XMLHttpRequest"
            }
        self.url = "https://www.lagou.com/jobs/positionAjax.json"

        # work information
        self.positionid = ""
        self.salary = ""
        self.positionName = ""
        self.isSchoolJob = ""
        self.workYear = ""
        self.positionLables = ""
        self.keyword = ""
        self.education = ""
        self.jobNature = ""
        self.businessZones = ""

        # company information
        self.companyid = ""
        self.city = ""
        self.companyFullName = ""
        self.industryField = ""
        self.financeStage = ""
        self.companySize = ""
        self.positionAdvantage = ""
        self.Longitude = ""
        self.latitude = ""

        # employment information
        self.createTime = ""

        self.counts = 0
        try:
            # get history recode data
            with open('recode/data.txt','r') as f:
                line = f.readlines()
                self.index = int(line[0].strip())
                self.currpage = int(line[1].strip())
                f.close()

                os.remove('recode/data.txt')
        except Exception as e:
            logging.error('读取数据失败%s'%(e))
            self.currpage = 0
            self.index = 0
        
        self.kds = ["PHP", 'C++', 'Java', '数据挖掘', '搜索算法', '精准推荐', 'C', 'C#', '全栈工程师', '.NET', 'Hadoop', 'Python',
                    'DelphiVB', 'Perl', 'Ruby', 'Node.js', 'Go', 'ASP', 'Shell', '后端开发其它HTML5',
                    'Android', 'iOS', 'WP', '移动开发其它',
                    'web前端', 'Flash', 'html5', 'JavaScript', 'U3D', 'COCOS2D-X', '前端开发其它',
                    '深度学习', '机器学习', '图像处理', '图像识别', '语音识别', '机器视觉', '算法工程师', '自然语言处理',
                    '测试工程师', '自动化测试', '功能测试', '性能测试', '测试开发', '游戏测试', '白盒测试', '灰盒测试', '黑盒测试', '手机测试', '硬件测试', '测试经理',
                    '测试其它',
                    '运维工程师', '运维开发工程师', '网络工程师', '系统工程师', 'IT支持', 'IDC', 'CDN', 'F5', '系统管理员', '病毒分析', 'WEB安全', '网络安全',
                    '系统安全', '运维经理', '运维其它',
                    'MySQL', 'SQLServer', 'Oracle', 'DB2', 'MongoDB', 'ETL', 'Hive', '数据仓库', 'DBA其它',
                    '技术经理', '技术总监',
                    '架构师', 'CTO', '运维总监', '技术合伙人', '项目总监', '测试总监', '安全专家', '高端技术职位其它',
                    '项目经理', '项目助理', '硬件', '嵌入式', '自动化', '单片机', '电路设计', '驱动开发', '系统集成', 'FPGA开发', 'DSP开发', 'ARM开发',
                    'PCB工艺',
                    '模具设计', '热传导', '材料工程师', '精益工程师', '射频工程师', '硬件开发其它',
                    '实施工程师', '售前工程师', '售后工程师', 'BI工程师', '企业软件其它']
        self.kd = self.kds[self.index]
    

    def request(self):

        post_data = {'frist': 'false', 'pn': self.currpage, 'kd': self.kd}

        try:
            request = requests.post(self.url, headers=self.header, data=post_data)
            try:
                jdict = json.loads(request.text)
                jcontent = jdict['content']
            except KeyError as e:
            	logging.error("关键字错误%s"%(e))
            	time.sleep(random.uniform(60,65))
            else:
	            jposresult = jcontent['positionResult']
	            jresult = jposresult['result']
	            self.counts = jposresult['totalCount']/15
	            for each in jresult:
	                # company information
	                self.companyid = each['companyId']
	                self.city = each['city']
	                self.companyFullName = each['companyFullName']
	                self.industryField = each['industryField']
	                self.financeStage = each['financeStage']
	                self.companySize = each['companySize']
	                self.positionAdvantage = each['positionAdvantage']
	                self.Longitude = each['longitude']
	                self.latitude = each['latitude']

	                # work information
	                self.positionid = each['positionId']
	                self.positionName = each['positionName']
	                self.isSchoolJob = each['isSchoolJob']
	                self.salary = each['salary']
	                self.workYear = each['workYear']
	                try:
	                    self.positionLables = ' '.join(each['positionLables'])
	                except:
	                    self.positionLables = 'None'
	                self.keyword = self.kd
	                self.education = each['education']
	                self.jobNature = each['jobNature']
	                try:
	                    self.businessZones = ' '.join(each['businessZones'])
	                except:
	                    self.businessZones = "None"

	                # employment information
	                self.createTime = each['createTime']

	                # insert employment
	                sql.insert_employment(sql.connect_db(), self.companyid, self.positionid, self.createTime)

	                # insert company
	                sql.insert_company(sql.connect_db(), self.companyid, self.city, self.companyFullName, self.industryField, self.financeStage,  self.companySize, self.positionAdvantage, self.Longitude, self.latitude)

	                # insert work
	                sql.insert_work(sql.connect_db(), self.positionid, self.positionName, self.salary, self.workYear, self.isSchoolJob, self.positionLables, self.keyword, self.education, self.jobNature, self.businessZones)

	            if self.currpage <= self.counts:
	                self.currpage = self.currpage + 1
	                logging.info("当前关键字%s - 爬到第%d页"%(self.kd,self.currpage))

	            elif self.index <= len(self.kds):
	                self.currpage = 0
	                self.counts = 0
	                self.index = self.index + 1
	                self.kd = self.kds[self.index]
	                time.sleep(random.random()*10)

        except Exception as e:
        	logging.error("网络异常 %s"%(e))
        	time.sleep(random.random()*100)
        except KeyboardInterrupt as e:
        	logging.error("用户外部中断，Ctrl+C，记录数据")
        	with open("recode/data.txt",'w') as f:
        		f.write('%s\n%s'%(self.index,self.currpage))
        		f.close()

        	logging.shutdown()
        	sys.exit(0)

sql = _Item()
scrapy = Snake()
while True:
	scrapy.request()
	



