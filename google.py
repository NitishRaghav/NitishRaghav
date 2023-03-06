import webbrowser
try:
    from googlesearch import search
except:
    print("Error in importing")
i=0
n=50
a=0
query=input("Enter what to search")

for j in search(query, tld="com", start=0, pause=2):
    while(i<n):
        
        if a != j:
            print(j)
            a=j
        i+=1
                 
    print("Thanks")
    exit()
