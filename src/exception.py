import sys
import logging


def error_msg_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    errormsg="Error occurred at filename [{0}] line number [{1}] error_msg[{2}]".format(filename,exc_tb.tb_lineno,str(error))
    return errormsg

class custom_exception(Exception):
    def __init__(self, error_msg,error_detail:sys):
        super().__init__(error_msg)
        self.error_msg=error_msg_details(error_msg,error_detail=error_detail)

    def __str__(self):
        return self.error_msg
    
# if __name__=="__main__":

#     try:
#         a= 1/0
#     except Exception as e:
#         logging.info("Divide by 0")
#         raise custom_exception(e,sys)
    

