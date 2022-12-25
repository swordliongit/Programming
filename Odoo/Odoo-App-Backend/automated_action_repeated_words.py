# Available variables:
#  - env: Odoo Environment on which the action is triggered
#  - model: Odoo Model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: Odoo function to compare floats based on specific precisions
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - UserError: Warning Exception to use with raise
#  - Command: x2Many commands namespace
# To return an action, assign: action = {...}


###########################
# bad words
bad_words = ["kötü", "berbat", "rezalet", "çok kötü", "leş", "maalesef", "iğrenç",
             "fena", "terbiyesiz", "bozuk", "kokmuş", "kokuşmuş", "uğursuz", "talihsiz",
             "aksi", "küfürlü", "rahatsız", "çürük", "zarar", "perişan", "şanssız",
             "sıkıcı", "sevimsiz", "aşağı", "çirkin", "kaba", "pis", "yetersiz",
             "yararsız", "beğenmedim", "cenabet", "iflah", "yaramaz", "döküntü", "itici",
             "yakışm", "donuk", "hoş değil", "iyi değil", "tuvalet", "gürültü",
             "banyo", "vasat", "asansör", "kirli", "zayıf", "kaygan", "fayans", "barlar",
             "sıkıntı", "temizlik",

             "bad", "worst", "hideous", "worse", "I hated", "substandard", "poor",
             "inferior", "second-class", "unsatisfactory", "inadequate", "unacceptable",
             "not up to par", "deficient", "unpleasant", "unwelcome", "unfortunate",
             "unfavourable", "unlucky", "adverse", "nasty", "terrible", "dreadful",
             "awful", "grim", "distressing", "regrettable", "faulty", "shoddy",
             "amateurish", "careless", "negligent", "abominable", "atrocious",
             "disgraceful", "hopeless", "worthless", "laughable", "miserable", "sorry",
             "third-rate", "incompetent", "inept", "rotten", "pathetic", "crummy",
             "useless", "woeful", "lousy", "appalling", "abysmal", "pitiful", "godawful",
             "dire", "duff", "rubbish", "egregious", "crap", "shit", "chickenshit", "too bad",
             "fake", "not good", "problem", "nah", "ass", "garbage", "wifi",
             "nope", "sucks", "toilet", "weird", "no", "donkey", "better", "crime",
             "busy", "leak", "outdated", "damage", "racist", "not a good", "horrible",
             "salty", "hard", "joke", "poop", "freezing", "disappointment", "room", "bathroom",
             "pool", "elevator", "bars",

                                 "несчастный", "позор", "очень жаль", "падаль",
             "сожалению", "отвратительный", "дурной", "нехорошо", "неудача", "дурно",
             "нехороший", "скверный", "вредный", "больной", "несчастье", "испорченный",
             "убыток", "недоброкачественный", "недействительный", "безнравственный",
             "гибель", "грубый", "дефицит", "разорение", "развращенный",
             "проблема", "отстой", "плохо", "ванная комната", "бары", "уборка",
             "огорченный", "слабый", "поднимать", "утюг", "туалет", "шум", "замораживание",
             "грязный",

             "schlecht", "schlimm", "böse", "übel", "schwer", "stark", "ungültig",
             "krank", "faul", "verdorben", "unartig", "mau", "verfault", "unanständig", "unrein",
             "ungedeckt", "ich hasste", "nicht", "keine", "nein", "toilette", "lärm", "eisen",
             "aufzug", "schmutzig", "schwach", "rutschig", "fliese", "reinigung"]

admin = env['analiz.profile'].search([('name', '=', 'Sonuçlar')])  # find the admin
contacts = env['analiz.profile'].search([])  # fetch all tables

one_w = False

if admin["x_repeat_list"]:  # check if the field is not empty
    repeat_list = admin["x_repeat_list"].split(",")  # divide the list of entered words

    found_badwords_list = []

    for contact in contacts:

        if isinstance(contact.comment,
                      str) and contact.comment != "" and "@" not in contact.comment and not contact.comment.isnumeric():

            contact["comment"] = contact.comment.lower()

            for word_to_find in repeat_list:  # fetch each element of the list
                if word_to_find in contact.comment and word_to_find in bad_words:
                    found_badwords_list.append(word_to_find)  # add what we find into the empty list

    output_list = []

    counter = 0

    for repeat_word, word_to_check in zip(repeat_list, found_badwords_list):
        counter = found_badwords_list.count(repeat_word)
        output_list.append(repeat_word + ": " + str(counter))

    admin["x_repeat_list_res"] = ",".join(output_list).replace(',', ' ')


else:
    admin["x_repeat_list_res"] = ""










