import json

# # รายการของ
# things = [
#     {
#         "name": "IMac", 
#         "price": 24, 
#     },
#     {
#         "name": "IPhone", 
#         "price": 15,
#     },
#     {
#         "name": "Mask", 
#         "price": 10,
#     },
#     {
#         "name": "Oven", 
#         "price": 5,
#     },
#     {
#         "name": "Voucher", 
#         "price": 1,
#     },
# ]

# customer_money = int(input())

answerList = []

def main(input_things, money):
    global answerList

    things = [
        {
            'name': i.split(',')[0].strip(),
            'price': int(i.split(',')[1])
        }
        for i in input_things
            # .replace('', '') # incase that we're using Unix new line
            .split('\r\n')[1:-1]
    ]

    customer_money = int(money)

    def getPossibility(recivedThings, money):

        global answerList # อย่าไปสนใจ อะไรที่เราไม่รู้จัก

        if money == 0: # เงินหมดแล้ว, print ความเป็นไปได้นี้
            if sorted(recivedThings) not in answerList:
                answerList.append(sorted(recivedThings))

        isSkipEverything = True # หยิบอะไรไม่ได้แล้ว หยิบครบทุกชิ้นแล้ว ?

        for thing in things: # ดูของแต่ละชิ้น

            if thing['name'] != 'Something Voucher' and recivedThings.count(thing['name']) >= 5: # หยิบ "ของ" ชนิดนี้มาเยอะแล้ว ให้คนอื่นบ้าง
                continue
            elif recivedThings.count(thing['name']) >= 20: # หยิบ "Voucher" มาเยอะแล้ว ให้คนอื่นบ้าง, Voucher มีทั้งหมด 4 แบบ หยิบได้แบบละ 5 อัน เหมารวมๆ Voucher เป็น 20 อัน จะได้ลดเวลาคำนวณ
                continue

            if money - thing['price'] >= 0: # เงินยังพอสำหรับของชิ้นนี้

                isSkipEverything = False # ยัง ยังไม่หมด ยังหยิบชิ้นนี้ได้

                getPossibility(recivedThings + [thing['name']], money - thing['price'])

        if isSkipEverything: # หยิบอะไรไม่ได้แล้ว ถือว่าของที่มีคือหยิบมาคือหยิบมาเท่าที่หยิบได้แล้ว, print ความเป็นไปได้นี้
            if sorted(recivedThings) not in answerList:
                answerList.append(sorted(recivedThings))

    getPossibility([], customer_money)

    possibilities = "Possibilities: {0} ".format(answerList)
    print(possibilities)
        
    print("Possibilities: ", len(answerList)) # แสดงความเป็นไปได้ทั้งหมด

    return json.dumps(
        {
            'possibilities_count': len(answerList),
            'possibilities': answerList
        }
    )

    # with open("result_%d.json" % customer_money, 'w') as file:
    #     file.write(json.dumps(answerList))


