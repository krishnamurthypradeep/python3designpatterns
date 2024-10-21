class Report:
    def __init__(self,content) -> None:
        
        self.content = content
    
    def generate(self):
        print(f"Report Content: {self.content}")
       
    # def save_to_file(self,filename):
    #     with open(filename , 'w') as file:
    #         file.write(self.content)
                    
class ReportSaver:
    
    def __init__(self,report: Report) -> None:
        
        self.report: Report = report
        
    def save_to_file(self,filename):
        with open(filename , 'w') as file:
            file.write(self.report.content)   
if __name__ == "__main__":
    content = "Some Contents For The Report "
    report = Report(content)
    report.generate()
    report_saver = ReportSaver(report)
    report_saver.save_to_file("report.txt")            
            
                             