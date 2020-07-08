import win32com.client
def fun():
    try:
        print("Enter your date of birth in Format\nDD MM YY:")
        speaker = win32com.client.Dispatch("SAPI.SpVoice") 
        speaker.Speak("Enter your date of birth in Format DATE,MONTH AND YEAR")
        a,b,c=input().split()
        num=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
        if a in num and int(c)>=2000:
            month_codes={"JAN":1,"FEB":4,"MAR":4,"APR":0,"MAY":2,"JUN":5,"JUL":0,"AUG":3,"SEP":6,"OCT":1,"NOV":4,"DEC":6}
            DAYS_CODES={0:"SAT",1:"SUN",2:"MON",3:"TUE",4:"WED",5:"THU",6:"FRI"}
            d=c[-1:-3:-1]
            e=d[::-1]
            res=int(a)+int(month_codes[b])+6+int(e)+(int(e)/4)
            y=int(res%7)
            print(DAYS_CODES[y])
        elif a in num and int(c)<2000:
            month_codes={"JAN":1,"FEB":4,"MAR":4,"APR":0,"MAY":2,"JUN":5,"JUL":0,"AUG":3,"SEP":6,"OCT":1,"NOV":4,"DEC":6}
            DAYS_CODES={0:"SAT",1:"SUN",2:"MON",3:"TUE",4:"WED",5:"THU",6:"FRI"}
            d=c[-1:-3:-1]
            e=d[::-1]
            res=int(a)+int(month_codes[b])+0+int(e)+(int(e)/4)
            y=int(res%7)
            print(DAYS_CODES[y])
        else:
            print("please enter valid date!!!")
    except ValueError:
        print("enter valid date")
    except KeyError:
        print("enter valid month")
