from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choose_course_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Выберите курс📚", callback_data="choose_course")]
    ]
)

courses_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Скорочтение и развитие интеллекта", callback_data="course_1")],
        [InlineKeyboardButton(text="Ментальная арифметика и ТРИЗ", callback_data="course_2")],
        [InlineKeyboardButton(text="Грамотное письмо и каллиграфия", callback_data="course_3")],
        [InlineKeyboardButton(text="Математика", callback_data="course_4")],
        [InlineKeyboardButton(text="Логопедия", callback_data="course_5")],
        [InlineKeyboardButton(text="Подготовка к школе", callback_data="course_6")],
        [InlineKeyboardButton(text="Секретная таблица умножения", callback_data="course_7")],
        [InlineKeyboardButton(text="Химия", callback_data="course_8")],
        [InlineKeyboardButton(text="Городской клуб", callback_data="course_9")],
        [InlineKeyboardButton(text="Английский язык", callback_data="course_10")]
    ]
)


gender_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Мальчик", callback_data="gender_m")],
        [InlineKeyboardButton(text="Девочка", callback_data="gender_f")]
    ]
)

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

back_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
])

levels_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Скорочтение. Маленький гений. 1 ступень",
            callback_data="level_1"
        )],
        [InlineKeyboardButton(
            text="Скорочтение. Маленький гений. 2 ступень",
            callback_data="level_2"
        )],
        [InlineKeyboardButton(
            text="Скорочтение. Маленький гений. 3 ступень",
            callback_data="level_3"
        )],
        [InlineKeyboardButton(
            text="Скорочтение. Юный гений. 4 ступень",
            callback_data="level_4"
        )],
        [InlineKeyboardButton(
            text="Скорочтение, точность восприятия информации. 5 ступень",
            callback_data="level_5"
        )],
    ]
)

menar_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Простое сложение и вычитание (Менар 1 ступень)",
            callback_data="menar_1"
        )],
        [InlineKeyboardButton(
            text="Сложение и вычитание (Менар 2 ступень)",
            callback_data="menar_2"
        )],
        [InlineKeyboardButton(
            text="Умножение, деление и отрицательные числа (Менар 3 ступень)",
            callback_data="menar_3"
        )],
        [InlineKeyboardButton(
            text="Иррациональные числа и корни (Менар 4 ступень)",
            callback_data="menar_4"
        )],
    ]
)

calligraphy_levels_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="1 уровень", callback_data="calligraphy_level_1"),
        InlineKeyboardButton(text="2 уровень", callback_data="calligraphy_level_2"),
        InlineKeyboardButton(text="3 уровень", callback_data="calligraphy_level_3"),
    ]
])

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

calligraphy_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="1 уровень",
            callback_data="calligraphy_level_1"
        )
    ],
    [
        InlineKeyboardButton(
            text="2 уровень",
            callback_data="calligraphy_level_2"
        )
    ],
    [
        InlineKeyboardButton(
            text="3 уровень",
            callback_data="calligraphy_level_3"
        )
    ]
])

math_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Сложение и вычитание (Математика на 5, 1 категория)",
            callback_data="math_1"
        )],
        [InlineKeyboardButton(
            text="Умножение и деление (Математика на 5, 2 категория)",
            callback_data="math_2"
        )],
        [InlineKeyboardButton(
            text="Вписать своё название программы (3 категория)",
            callback_data="math_custom"
        )],
    ]
)

chemistry_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Юный Химик", callback_data="chem_1")],
        [InlineKeyboardButton(text="Ассистент по Химии", callback_data="chem_2")],
        [InlineKeyboardButton(text="Адепт Химии", callback_data="chem_3")],
        [InlineKeyboardButton(text="Бакалавр Химии", callback_data="chem_4")],
        [InlineKeyboardButton(text="Магистр Химии", callback_data="chem_5")],
        [InlineKeyboardButton(text="Мастер Химии", callback_data="chem_6")],
    ]
)


# уровень английского
english_level_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="ABC-club", callback_data="eng_abc")],
    [InlineKeyboardButton(text="School-club", callback_data="eng_school")],
    [InlineKeyboardButton(text="Teens-club", callback_data="eng_teens")]
])

# school: тип теста
eng_school_test_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Тест по УМК", callback_data="eng_test_umk")],
    [InlineKeyboardButton(text="Тест на уровень", callback_data="eng_test_level")]
])

# base уровни school
eng_school_base_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Pre-A1", callback_data="eng_base_pre_a1")],
    [InlineKeyboardButton(text="A1", callback_data="eng_base_a1")],
    [InlineKeyboardButton(text="A2", callback_data="eng_base_a2")],
    [InlineKeyboardButton(text="B1", callback_data="eng_base_b1")]
])

# base уровни teens
eng_teens_base_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="A1", callback_data="eng_base_a1")],
    [InlineKeyboardButton(text="A2", callback_data="eng_base_a2")],
    [InlineKeyboardButton(text="B1", callback_data="eng_base_b1")],
    [InlineKeyboardButton(text="B2", callback_data="eng_base_b2")],
    [InlineKeyboardButton(text="C1", callback_data="eng_base_c1")],
    [InlineKeyboardButton(text="C2", callback_data="eng_base_c2")]
])

# skill уровни (одни и те же для всех)
eng_skill_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Pre-A1", callback_data="eng_skill_pre_a1"),
        InlineKeyboardButton(text="A1", callback_data="eng_skill_a1")
    ],
    [
        InlineKeyboardButton(text="A2", callback_data="eng_skill_a2"),
        InlineKeyboardButton(text="B1", callback_data="eng_skill_b1")
    ]
])



InlineKeyboardButton(
    text="Подготовка к школе",
    callback_data="course_6"
)


InlineKeyboardButton(
    text="Таблица умножения",
    callback_data="course_7"
)

speed_app_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="✅ Да", callback_data="speed_app_yes")],
        [InlineKeyboardButton(text="❌ Нет", callback_data="speed_app_no")]
    ]
)