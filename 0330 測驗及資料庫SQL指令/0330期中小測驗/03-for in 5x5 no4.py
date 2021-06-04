for x in range(1,6):
    if x!=4:
        for y in range(1,6):
            if y!=4:
                ans=x*y
                print(x,"*",y,"=",ans)
            else:
                print("")

    else:
        print("")