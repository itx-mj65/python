import os
def genrate_table(num):
    table=""
    for i in range(1,11):
        table +=f"{num} X {i} = {num*i}\n"
    os.makedirs("tables", exist_ok=True)
    print(table)
    with open(f"tables/table_{num}.txt", "w") as f:
        f.write(table)


for i in range(1,11):
    print(i, end=" ")
    genrate_table(i)