FROM python:3.7
copy . . 
ENV strings="aba,baba,aba,xzxb"
ENTRYPOINT [ "python" ,"main.py"]