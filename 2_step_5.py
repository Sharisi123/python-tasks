import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp('Олександр Наживотов')

number = '24'
date = '30.01.2021'
name = 'Наживотов Iван Сергiйович'

a = f"""
---------------------------------------------------------------------
            Рахунок-фактура № {number} вiд {date}
---------------------------------------------------------------------
ПОСТАЧАЛЬНИК:                  Платник: ЧП {name}
Управлiння Iнженерного захисту 
територii мiста та розвитку 
узбережжя ОМР Код ЭДРПОУ
24760454 Р/р №: 3453132421
МФО 828011 в ГУДКУ в Одеськiй областi


Пiдстава: 
---------------------------------------------------------------------
| № |    Найменнування товару     | Од.вим. | Кiльк. | Цiна  | Сума |
|   | Узгодження проектноi        |         |        |       |      |
|   | документацii нового         |  услуг  | 1.00   | 0.00  | 0.00 |
|   | будiвництва за адресою      |         |        |       |      |
|   | м.Одеса, вул.Iванова, 896   |         |        |       |      |
---------------------------------------------------------------------
                                              Всього без ПДВ | 0.00 |
                                                         ПДВ | 0.00 |
                                           Всього сума з ПДВ |      |
                                                             --------
 """    

print(a)