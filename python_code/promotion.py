import json
import copy


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

    all_money = [
        int(j)
        
    for j in money
        .split('\r\n')[1:-1]
    ]

    money_answers = []

    for money in all_money:
        answerList = []

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

        getPossibility([], money)

        possibilities = "Possibilities: {0} ".format(answerList)
        print(possibilities)
            
        print("Possibilities: ", len(answerList)) # แสดงความเป็นไปได้ทั้งหมด

        money_answers.append(
                {
                    'money': money,
                    'possibilities_count': len(answerList),
                    'possibilities': copy.deepcopy(answerList)
                }
            )
        
       
    return json.dumps(money_answers)



