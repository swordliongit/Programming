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


# good words
comment_filter_g_TR = ["iyi", "çok iyi", "mükemmel", "fevkalade", "güzel",
                       "muhteşem", "muazzam", "pek iyi", "fena değil", "beğendim", "aferin",
                       "harika", "ideal", "harikulade", "kusursuz", "şahane", "müthiş",
                       "on numara", "hoş", "berceste", "latif", "rana", "rakik", "onay",
                       "uygun", "gözüm tuttu", "takdir", "tasvip", "iltifat", "razı",
                       "teşekkür", "süper", "4 yıldız", "dört yıldız", "5 yıldız", "beş yıldız",
                       "evet", "memnun", "başarılı", "barlar"]

comment_filter_g_EN = ["perfect", "good", "very good", "amazing", "gorgeous", "nice",
                       "not bad", "super", "thank", "polite", "helpful", "best", "cheap",
                       "awful", "liked", "all right", "fine", "positive", "very well",
                       "cunning", "worth", "competent", "neat", "great", "out of this world",
                       "cute", "clean", "thanks", "excellent", "exceptional", "favorable",
                       "marvelous", "satisf", "fantastic", "cool", "top", "thx", "beautiful",
                       "come back", "4 star", "four star", "5 star", "five star", "fun", "yes",
                       "yup", "yep", "brilliant", "enjoy", "successful", "favorite",
                       "favourite", "love", "smil", "wow", "awesome"]

comment_filter_g_RU = ["супер", "благо", "добро", "польза", "хорошо", "хороший", "добрый",
                       "приятный", "благой", "доброкачественный", "благоприятный", "здоровый",
                       "полезный", "надежный", "значительный", "милый", "надлежащий", "годный",
                       "любезный", "добродетельный", "умелый", "искусный", "свежий", "послушный",
                       "сытный", "уважительный", "плодородный", "неиспорченный", "кредитоспособный",
                       "да", "спасибо", "замечательно", "понравилось", "успешный", "ок", "успехов"]

comment_filter_g_DE = ["perfekt", "nutzen", "vorteil", "heil", "wert", "gut", "schön",
                       "geeignet", "angenehm", "brav", "nützlich", "gesund", "artig", "lieb",
                       "froh", "frisch", "ehrlich", "reich", "günstig", "gescheit", "wohl",
                       "jut", "fromm", "von guter qualität", "zuverlässig", "ausreichend",
                       "nett", "sauber", "hübsch", "fein", "sympathisch", "lecker", "genau", "dank",
                       "heikel", "ich mochte", "alles gut", "alles", "sehr gut", "süß", "toll",
                       "hinreißend", "atemberaubend"]

###########################
# bad words
comment_filter_b_TR = ["kötü", "berbat", "rezalet", "çok kötü", "leş", "maalesef", "iğrenç",
                       "fena", "terbiyesiz", "bozuk", "kokmuş", "kokuşmuş", "uğursuz", "talihsiz",
                       "aksi", "küfürlü", "rahatsız", "çürük", "zarar", "perişan", "şanssız",
                       "sıkıcı", "sevimsiz", "aşağı", "çirkin", "kaba", "pis", "yetersiz",
                       "yararsız", "beğenmedim", "cenabet", "iflah", "yaramaz", "döküntü", "itici",
                       "yakışm", "donuk", "hoş değil", "iyi değil", "tuvalet", "havuz",
                       "banyo", "vasat", "asansör", "kirli", "gürültü", "zayıf", "kaygan", "fayans",
                       "sıkıntı", "temizlik"]

comment_filter_b_EN = ["bad", "worst", "hideous", "worse", "I hated", "substandard", "poor",
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
                       "salty", "hard", "joke", "poop", "freezing", "disappointment", "pool",
                       "room", "bathroom", "elevator", "bars"]

comment_filter_b_RU = ["несчастный", "позор", "очень жаль", "падаль",
                       "сожалению", "отвратительный", "дурной", "нехорошо", "неудача", "дурно",
                       "нехороший", "скверный", "вредный", "больной", "несчастье", "испорченный",
                       "убыток", "недоброкачественный", "недействительный", "безнравственный",
                       "гибель", "грубый", "дефицит", "разорение", "развращенный",
                       "проблема", "отстой", "плохо", "ванная комната", "бары", "уборка",
                       "огорченный", "слабый", "поднимать", "утюг", "туалет", "шум", "замораживание",
                       "грязный"]

comment_filter_b_DE = ["schlecht", "schlimm", "böse", "übel", "schwer", "stark", "ungültig",
                       "krank", "faul", "verdorben", "unartig", "mau", "verfault", "unanständig", "unrein",
                       "ungedeckt", "ich hasste", "nicht", "keine", "nein", "toilette", "lärm", "eisen",
                       "aufzug", "schmutzig", "schwach", "rutschig", "fliese", "reinigung"]

# starting with zero

points_nan = 0  # invalid comments
points_neutr = 0  # neutral comments
points_good = 0
points_bad = 0

# for calculating percentage

score_good = 0
score_bad = 0
score_neutr = 0

# g : good  b : bad

TR_g = 0
TR_b = 0
EN_g = 0
EN_b = 0
RU_g = 0
RU_b = 0
DE_g = 0
DE_b = 0

num_of_valid_words = 0
num_of_valid_comments = 0
comments_total = 0

"""
# Repeat counter app
TR_b_list = []
EN_b_list = []
RU_b_list = []
DE_b_list = []
"""

# main loop for score calculation

contacts = env['analiz.profile'].search([])

for contact in contacts:
    comments_total += 1

    if isinstance(contact.comment,
                  str) and contact.comment != "" and "@" not in contact.comment and not contact.comment.isnumeric():

        num_of_valid_comments += 1
        contact["comment"] = contact.comment.lower()

        for good in comment_filter_g_TR:
            if good in contact.comment:
                TR_g += 1
                num_of_valid_words += 1
                log(contact.comment + " TR", level="info")
                contact["x_TR_g"] = 1
                break

        for good in comment_filter_g_EN:
            if good in contact.comment:
                EN_g += 1
                num_of_valid_words += 1
                log(contact.comment + " EN", level="info")
                contact["x_EN_g"] = 1
                break

        for good in comment_filter_g_DE:
            if good in contact.comment:
                DE_g += 1
                num_of_valid_words += 1
                log(contact.comment + " DE", level="info")
                contact["x_DE_g"] = 1
                break

        for good in comment_filter_g_RU:
            if good in contact.comment:
                RU_g += 1
                num_of_valid_words += 1
                log(contact.comment + " RU", level="info")
                contact["x_RU_g"] = 1
                break

        ################### bad word finder starts here ######################

        for bad in comment_filter_b_TR:
            if bad in contact.comment:
                # TR_b_list.append(bad)
                TR_b += 1
                num_of_valid_words += 1
                log(contact.comment + " TR", level="info")
                contact["x_TR_b"] = 1
                break

        for bad in comment_filter_b_EN:
            if bad in contact.comment:
                # EN_b_list.append(bad)
                EN_b += 1
                num_of_valid_words += 1
                log(contact.comment + " EN", level="info")
                contact["x_EN_b"] = 1
                break

        for bad in comment_filter_b_DE:
            if bad in contact.comment:
                # DE_b_list.append(bad)
                DE_b += 1
                num_of_valid_words += 1
                log(contact.comment + " DE", level="info")
                contact["x_DE_b"] = 1
                break

        for bad in comment_filter_b_RU:
            if bad in contact.comment:
                # RU_b_list.append(bad)
                RU_b += 1
                num_of_valid_words += 1
                log(contact.comment + " RU", level="info")
                contact["x_RU_b"] = 1
                break

    else:
        points_nan += 1

# calculate points
points_good = TR_g + EN_g + RU_g + DE_g
points_bad = TR_b + EN_b + RU_b + DE_b

points_neutr = num_of_valid_comments - num_of_valid_words

# calculate percentages
score_good = round(points_good / num_of_valid_comments * 100, 2)
score_bad = round(points_bad / num_of_valid_comments * 100, 2)
score_neutr = round(points_neutr / num_of_valid_comments * 100, 2)

"""
# Repeat counter app : find which bad words were repeated the most and how many times it were
max_TR_b = max(TR_b_list)
count_max_TR_b = TR_b_list.count(max_TR_b)

second_TR_b_list = [i for i in TR_b_list if i != max_TR_b]
second_max_TR_b = max(second_TR_b_list)
count_second_max_TR_b = second_TR_b_list.count(second_max_TR_b)

third_TR_b_list = [i for i in second_TR_b_list if i != second_max_TR_b]
third_max_TR_b = max(third_TR_b_list)
count_third_max_TR_b = third_max_TR_b.count(third_max_TR_b)



max_EN_b = max(EN_b_list)
count_max_EN_b = EN_b_list.count(max_EN_b)

second_EN_b_list = [i for i in EN_b_list if i != max_EN_b]
second_max_EN_b = max(second_EN_b_list)
count_second_max_EN_b = second_EN_b_list.count(second_max_EN_b)

third_EN_b_list = [i for i in second_EN_b_list if i != second_max_EN_b]
third_max_EN_b = max(third_EN_b_list)
count_third_max_EN_b = third_max_EN_b.count(third_max_EN_b)



max_RU_b = max(RU_b_list)
count_max_RU_b = RU_b_list.count(max_RU_b)

second_RU_b_list = [i for i in RU_b_list if i != max_RU_b]
second_max_RU_b = max(second_RU_b_list)
count_second_max_RU_b = second_RU_b_list.count(second_max_RU_b)

third_RU_b_list = [i for i in second_RU_b_list if i != second_max_RU_b]
third_max_RU_b = max(third_RU_b_list)
count_third_max_RU_b = third_max_RU_b.count(third_max_RU_b)



max_DE_b = max(DE_b_list)
count_max_DE_b = DE_b_list.count(max_DE_b)

second_DE_b_list = [i for i in DE_b_list if i != max_DE_b]
second_max_DE_b = max(second_DE_b_list)
count_second_max_DE_b = second_DE_b_list.count(second_max_DE_b)

third_DE_b_list = [i for i in second_DE_b_list if i != second_max_DE_b]
third_max_DE_b = max(third_DE_b_list)
count_third_max_DE_b = third_max_DE_b.count(third_max_DE_b)
"""

# find the admin
admin = env["analiz.profile"].search([("name", "=", "Sonuçlar")], limit=1)

# write into admin's fields
admin["x_score_good"] = score_good
admin["x_score_bad"] = score_bad
admin["x_score_neutr"] = score_neutr
admin["x_comments_total"] = comments_total
admin["x_points_good"] = points_good
admin["x_points_bad"] = points_bad
admin["x_points_neutr"] = points_neutr
admin["x_points_nan"] = points_nan
admin["x_TR_g"] = TR_g
admin["x_TR_b"] = TR_b
admin["x_EN_g"] = EN_g
admin["x_EN_b"] = EN_b
admin["x_RU_g"] = RU_g
admin["x_RU_b"] = RU_b
admin["x_DE_g"] = DE_g
admin["x_DE_b"] = DE_b

"""
# Repeat counter app
admin["x_max_TR_b"] = max_TR_b
admin["x_count_max_TR_b"] = count_max_TR_b
admin["x_second_max_TR_b"] = second_max_TR_b
admin["x_count_second_max_TR_b"] = count_second_max_TR_b
admin["x_third_max_TR_b"] = third_max_TR_b
admin["x_count_third_max_TR_b"] = count_third_max_TR_b

admin["x_max_EN_b"] = max_EN_b
admin["x_count_max_EN_b"] = count_max_EN_b
admin["x_second_max_EN_b"] = second_max_EN_b
admin["x_count_second_max_EN_b"] = count_second_max_EN_b
admin["x_third_max_EN_b"] = third_max_EN_b
admin["x_count_third_max_EN_b"] = count_third_max_EN_b

admin["x_max_RU_b"] =  second_max_RU_b
admin["x_count_max_RU_b"] = count_second_max_RU_b
admin["x_second_max_RU_b"] = max_RU_b
admin["x_count_second_max_RU_b"] = count_max_RU_b
admin["x_third_max_RU_b"] = third_max_RU_b
admin["x_count_third_max_RU_b"] = count_third_max_RU_b

admin["x_max_DE_b"] = max_DE_b
admin["x_count_max_DE_b"] = count_max_DE_b
admin["x_second_max_DE_b"] = second_max_DE_b
admin["x_count_second_max_DE_b"] = count_second_max_DE_b
admin["x_third_max_DE_b"] = third_max_DE_b
admin["x_count_third_max_DE_b"] = count_third_max_DE_b
"""

# print the calculated score
log("İyi yorum oranı: %" + str(score_good) + "\n"
    + "Kötü yorum oranı: %" + str(score_bad) + "\n"
    + "Nötr yorum oranı: %" + str(score_neutr) + "\n"
    + "Toplam yorum sayısı: " + str(comments_total) + "\n"
    + "İyi yorum sayısı: " + str(points_good) + "\n"
    + "Kötü yorum sayısı: " + str(points_bad) + "\n"
    + "Nötr yorum sayısı: " + str(points_neutr) + "\n"
    + "Anlamsız yorum sayısı: " + str(points_nan) + "\n"
    + "Türkçe iyi yorum sayısı: " + str(TR_g) + "\n"
    + "Türkçe kötü yorum sayısı: " + str(TR_b) + "\n"
    + "İngilizce iyi yorum sayısı: " + str(EN_g) + "\n"
    + "İngilizce kötü yorum sayısı: " + str(EN_b) + "\n"
    + "Rusça iyi yorum sayısı: " + str(RU_g) + "\n"
    + "Rusça kötü yorum sayısı: " + str(RU_b) + "\n"
    + "Almanca iyi yorum sayısı: " + str(DE_g) + "\n"
    + "Almanca kötü yorum sayısı: " + str(DE_b), level='info')

# log("Total number of found valid comments: " + str(num_of_valid_comments), level = "info")
# log("Total number of found valid words: " + str(num_of_valid_words), level = "info")






