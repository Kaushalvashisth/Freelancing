start_Html="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" 
    rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" 
    crossorigin="anonymous">
    
    <title>Table Creator</title>
    
</head>
<body>
    <div class="container">
		<h1 class="diplay-1 text-center text-primary pt-4 pb-3" style="letter-spacing:5rem;">
            DASHBOARD
        </h1>
"""
col_start="""
        <div class="img-thumbnail img-fluid" style="width: {0}%; margin-right: 1%;">
"""
col_end="""
        </div>    
"""
rowStart="""
    <div class="row" style="padding: 10px;">
"""
rowEnd="""
    </div>
"""
endHtml="""
</div>
</body>
</html>
"""


def addRow(col,row):
    global start_Html
    global col_start
    global rowStart
    global rowEnd
    global endHtml
    # specify col size here
    col_width=int(100/col)-1
    # row
    start_Html+=rowStart

    # columns
    for j in range(1,col+1):
        print("\nEnter content of row:",row,"and col:",j," ")
        col_input="""         """+str(input())

        start_Html+=col_start.format(col_width)
        start_Html+=col_input
        start_Html+=col_end

    start_Html+=rowEnd

def generateHtml():
    global start_Html
    start_Html+=endHtml
    hs = open("Genrated.html", 'w')
    hs.write(start_Html)

if __name__ == "__main__":
    row=int(input("Enter number of rows: "))
    for i in range(1,row+1):
        print("\nEnter number of columns in ",i," row")
        col=int(input())
        addRow(col,i)
    generateHtml()

