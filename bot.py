import asyncio
import os
from pathlib import Path
from aiogram.types import FSInputFile
BASE_DIR = Path(__file__).resolve().parent
from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from pdf.generate import generate_certificate_from_template
from keyboards.inline import choose_course_kb, courses_kb, gender_kb, levels_kb, menar_kb, calligraphy_kb, math_kb, chemistry_kb, english_level_kb
from config import BOT_TOKEN
from pdf.maps import SPEED_READING_MAP
from pdf.maps import COURSE_MAP
from pdf.maps import MENTAL_ARITHMETIC_MAP
from pdf.maps import CALLIGRAPHY_MAP
from pdf.maps import MATH_MAP
from pdf.maps import SIMPLE_TEMPLATES
from pdf.maps import SPEECH_THERAPY_MAP
from pdf.maps import SCHOOL_PREP_MAP
from pdf.maps import MULTIPLICATION_TABLE_MAP
from pdf.maps import CHEMISTRY_MAP
from pdf.maps import SPEED_READING_APPENDIX_MAP
from pdf.maps import CITY_CLUB_MAP
from pdf.maps import ENGLISH_MAP
from keyboards.reply import start_kb
from aiogram.filters import Command
from keyboards.inline import back_kb
from keyboards.inline import speed_app_kb
from keyboards.inline import (
    choose_course_kb,
    courses_kb,
    gender_kb,
    levels_kb,
    menar_kb,
    calligraphy_kb,
    math_kb,
    chemistry_kb,
    english_level_kb,
    eng_school_test_kb,
    eng_teens_base_kb,
    english_level_kb,
    eng_teens_base_kb,
    eng_school_test_kb,
    eng_skill_kb,
    eng_school_base_kb
)
# ================= FSM =================

class CertificateFSM(StatesGroup):
    student_name = State()
    gender = State()
    teacher = State()
    hours = State()
    date_start = State()
    date_end = State()
    year = State()
    level = State()
    custom_program = State()
    eng_total = State()
    eng_score = State()
    eng_reading = State()
    speech_program = State()
    goal = State()
    eng_test_type = State()
    eng_umk_level = State()
    eng_base_level = State()
    eng_listening = State()
    eng_speaking = State()
    eng_writing = State()
    gender = State()
    start_date = State()
    end_date = State()
    year = State()
    program_name = State()

    reading_before = State()
    reading_after = State()

    mnemo_before = State()
    mnemo_after = State()

    visual_before = State()
    visual_after = State()

    image_before = State()
    image_after = State()

    dynamic_before = State()
    dynamic_after = State()


# ================= DATA =================

COURSES = {
    "1": "Скорочтение и развитие интеллекта",
    "2": "Ментальная арифметика и ТРИЗ",
    "3": "Грамотное письмо и каллиграфия",
    "4": "Математика",
    "5": "Логопедия",
    "6": "Подготовка к школе",
    "7": "Секретная таблица умножения",
    "8": "Химия",
    "9": "Городской клуб",
    "10": "Английский язык"
}

COURSES_WITH_DATES = [
    "Скорочтение и развитие интеллекта",
    "Ментальная арифметика и ТРИЗ",
    "Грамотное письмо и каллиграфия",
    "Математика",
    "Логопедия",
    "Подготовка к школе",
    "Секретная таблица умножения"
]

MENAR_LEVELS = {
    "1": "Простое сложение и вычитание (Менар 1 ступень)",
    "2": "Сложение и вычитание (Менар 2 ступень)",
    "3": "Умножение, деление и отрицательные числа (Менар 3 ступень)",
    "4": "Иррациональные числа и корни (Менар 4 ступень)"
}

# ================= BOT =================

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# /start
@dp.message(Command("start"))
async def start_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Добро пожаловать! 🎓\n\nВыберите курс:",
        reply_markup=start_kb
    )
    await message.answer(
        "Доступные курсы:",
        reply_markup=courses_kb
    )
# Выбор курса
@dp.callback_query(F.data == "choose_course")
async def choose_course(callback: CallbackQuery):
    await callback.message.answer(
        "Выберите курс 🙂",
        reply_markup=courses_kb
    )
    await callback.answer()




@dp.callback_query(F.data == "back")
async def go_back(callback: CallbackQuery, state: FSMContext):
    current_state = await state.get_state()

    back_map = {
        CertificateFSM.year: CertificateFSM.student_name,
        CertificateFSM.student_name: CertificateFSM.course,
        CertificateFSM.gender: CertificateFSM.level,
        CertificateFSM.level: CertificateFSM.course,
    }

    prev_state = back_map.get(current_state)

    if not prev_state:
        await callback.message.answer("Вы уже в начале 🚀")
        return

    await state.set_state(prev_state)

    # Сообщения для каждого шага
    messages = {
        CertificateFSM.student_name: "Введите имя ученика:",
        CertificateFSM.course: "Выберите курс:",
        CertificateFSM.level: "Выберите уровень:",
        CertificateFSM.gender: "Выберите пол:",
        CertificateFSM.year: "Введите год:",
    }

    await callback.message.answer(messages[prev_state])
    await callback.answer()


# Курс выбран
@dp.callback_query(F.data.startswith("course_"))
async def course_selected(callback: CallbackQuery, state: FSMContext):
    course_code = callback.data.replace("course_", "")  # "1", "2", "3"
    course_name = COURSES[course_code]

    await state.update_data(
        course_code=course_code,   # ← ВАЖНО
        course_name=course_name,
        reply_markup=back_kb
        
    )

    await callback.message.answer(
        f"Вы выбрали курс: {course_name}\nВведите ФИО ученика:"
    )
    await state.set_state(CertificateFSM.student_name)
    await callback.answer()

# ФИО ученика
@dp.message(CertificateFSM.student_name)
async def student_name_handler(message: Message, state: FSMContext):
    name = message.text.upper()
    await state.update_data(student_name=name)

    data = await state.get_data()
    course_name = data["course_name"]

    # СПЕЦИАЛЬНАЯ ЛОГИКА ДЛЯ СКОРОЧТЕНИЯ
    if course_name == "Скорочтение и развитие интеллекта":
        await message.answer(
            "Выберите ступень обучения:",
            reply_markup=levels_kb
        )
        await state.set_state(CertificateFSM.level)
        return

    # МЕНТАЛЬНАЯ АРИФМЕТИКА И ТРИЗ
    if course_name == "Ментальная арифметика и ТРИЗ":
        await message.answer(
            "Выберите программу обучения:",
            reply_markup=menar_kb
        )
        await state.set_state(CertificateFSM.level)
        return

    # ГРАМОТНОЕ ПИСЬМО И КАЛЛИГРАФИЯ
    if course_name == "Грамотное письмо и каллиграфия":
        await message.answer(
            "Выберите уровень программы:",
            reply_markup=calligraphy_kb
        )
        await state.set_state(CertificateFSM.level)
        return

    # МАТЕМАТИКА
    if course_name == "Математика":
        await message.answer(
            "Выберите программу обучения:",
            reply_markup=math_kb
        )
        await state.set_state(CertificateFSM.level)
        return

    # ЛОГОПЕДИЯ
    if course_name == "Логопедия":
        await message.answer(
            "Введите название программы.\n"
            "например: по постановке звуков «Л» и «Р»"
        )
        await state.set_state(CertificateFSM.custom_program)
        return

    # ХИМИЯ
    if course_name == "Химия":
        await message.answer(
            "Выберите уровень обучения:",
            reply_markup=chemistry_kb
        )
        await state.set_state(CertificateFSM.level)
        return
    
    # АНГЛИЙСКИЙ ЯЗЫК
    if course_name == "Английский язык":
        await message.answer(
            "Выберите уровень:",
            reply_markup=english_level_kb
        )
        await state.set_state(CertificateFSM.level)
        return

    # Городской клуб — без пола и педагога
    if course_name == "Городской клуб":
        await message.answer(
            "Выберите пол ученика:",
            reply_markup=gender_kb
        )
        await state.set_state(CertificateFSM.gender)
        return

    # Остальные курсы
    await message.answer(
        "Выберите пол ученика:",
        reply_markup=gender_kb
    )
    await state.set_state(CertificateFSM.gender)



@dp.message(F.text == "🔄 Начать новый сертификат")
async def restart_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Выберите курс для генерации сертификата:",
        reply_markup=start_kb
    )
    await message.answer(
        "Доступные курсы:",
        reply_markup=courses_kb
    )
# Пол
@dp.callback_query(F.data.startswith("gender_"), CertificateFSM.gender)
async def gender_handler(callback: CallbackQuery, state: FSMContext):
    gender_map = {
        "m": "boy",
        "f": "girl"
    }

    gender_code = callback.data.split("_")[1]
    gender = gender_map[gender_code]
    await state.update_data(gender=gender)

    data = await state.get_data()
    course_name = data.get("course_name")   # или course_code

    # 🔹 ГОРОДСКОЙ КЛУБ — ПРОПУСКАЕМ ВСЁ
    if course_name == "Городской клуб":
        await callback.message.answer(
            "Введите название программы:"
        )
        await state.set_state(CertificateFSM.program_name)

    else:
        # 🔹 ВСЕ ОСТАЛЬНЫЕ
        await callback.message.answer(
            "Введите фамилию и инициалы педагога:"
        )
        await state.set_state(CertificateFSM.teacher)

    await callback.answer()

 # ступень скорочтение
@dp.callback_query(F.data.startswith("level_"), CertificateFSM.level)
async def level_selected(callback: CallbackQuery, state: FSMContext):
    levels = {
        "1": "Скорочтение. Маленький гений. 1 ступень",
        "2": "Скорочтение. Маленький гений. 2 ступень",
        "3": "Скорочтение. Маленький гений. 3 ступень",
        "4": "Скорочтение. Юный гений. 4 ступень",
        "5": "Скорочтение, точность восприятия информации. 5 ступень",
    }

    level_id = callback.data.split("_")[1]   # ← "1"
    level_name = levels[level_id]            # ← красивое название

    await state.update_data(
        level_id=level_id,        # ← ВАЖНО: номер!
        level_name=level_name  # ← название для PDF
    )

    await callback.message.answer(
        f"Вы выбрали:\n{level_name}\n\nВыберите пол ученика:",
        reply_markup=gender_kb
    )

    await state.set_state(CertificateFSM.gender)
    await callback.answer()



#ментальная и триз
@dp.callback_query(F.data.startswith("menar_"))
async def menar_level_selected(callback: CallbackQuery, state: FSMContext):
    level_id = callback.data.replace("menar_", "")
    level_name = MENAR_LEVELS[level_id]

    await state.update_data(
        level_id=level_id,   # 🔑 для MAP
        level=level_name     # 🖨 для текста в PDF
    )

    await callback.message.answer(
        "Выберите пол ученика:",
        reply_markup=gender_kb
    )
    await state.set_state(CertificateFSM.gender)
    await callback.answer()

#каллиграфия
@dp.callback_query(F.data.startswith("calligraphy_level_"))
async def calligraphy_level_handler(callback: CallbackQuery, state: FSMContext):
    print("🔥 CALLIGRAPHY LEVEL CALLBACK:", callback.data)

    # 👉 вытаскиваем номер уровня
    level_id = callback.data.split("_")[-1]  # "1" | "2" | "3"

    # 👉 СОХРАНЯЕМ ИМЕННО level_id
    await state.update_data(level_id=level_id)

    await callback.message.answer(
        "Выберите пол ученика:",
        reply_markup=gender_kb
    )

    await state.set_state(CertificateFSM.gender)
    await callback.answer()


#математика
@dp.callback_query(F.data.startswith("math_"), CertificateFSM.level)
async def math_selected(callback: CallbackQuery, state: FSMContext):
    level_id = callback.data.split("_")[-1]  # "1" | "2" | "custom"

    # ---------- ГОТОВЫЕ ПРОГРАММЫ ----------
    if level_id == "1":
        await state.update_data(
            level_id="1",
            level="Сложение и вычитание (Свидетельство Математика на 5, 1 категория)"
        )

    elif level_id == "2":
        await state.update_data(
            level_id="2",
            level="Умножение и деление (Свидетельство Математика на 5, 2 категория)"
        )

    # ---------- КАСТОМНАЯ ПРОГРАММА ----------
    elif level_id == "custom":
        await state.update_data(level_id="3")  # ← ВАЖНО!!!
        await callback.message.answer("Введите название программы:")
        await state.set_state(CertificateFSM.custom_program)
        await callback.answer()
        return

    # ---------- ДАЛЬШЕ ДЛЯ ГОТОВЫХ ----------
    await callback.message.answer(
        "Выберите пол ученика:",
        reply_markup=gender_kb
    )
    await state.set_state(CertificateFSM.gender)
    await callback.answer()

# математика кастом
@dp.message(CertificateFSM.custom_program)
async def custom_program_handler(message: Message, state: FSMContext):
    program_name = message.text.strip()

    await state.update_data(
        program_name=program_name,  # ← ВАЖНО
        level=f"{program_name} (Свидетельство Математика на 5, 3 категория)"
    )

    await message.answer(
        "Выберите пол ученика:",
        reply_markup=gender_kb
    )
    await state.set_state(CertificateFSM.gender)


@dp.message(CertificateFSM.program_name)
async def program_name_handler(message: Message, state: FSMContext):
    await state.update_data(program_name=message.text)
    await message.answer("Введите дату начала занятий (например: 31.05.2025):")
    await state.set_state(CertificateFSM.date_start)


# логопедия
@dp.callback_query(F.data == "course_5")
async def speech_start(callback: CallbackQuery, state: FSMContext):
    await state.update_data(course_code="5", course_name="Логопедия")

    await callback.message.answer(
        "Введите название программы по логопедии:"
    )
    await state.set_state(CertificateFSM.speech_program)
    await callback.answer()

@dp.message(CertificateFSM.speech_program)
async def speech_program_handler(message: Message, state: FSMContext):
    await state.update_data(program_name=message.text)

    await message.answer(
        "Выберите пол ученика:",
        reply_markup=gender_kb
    )
    await state.set_state(CertificateFSM.gender)


@dp.callback_query(F.data.startswith("chem_"), CertificateFSM.level)
async def chemistry_selected(callback: CallbackQuery, state: FSMContext):
    levels = {
        "1": "Юный химик",
        "2": "Ассистент по химии",
        "3": "Адепт химии",
        "4": "Бакалавр химии",
        "5": "Магистр химии",
        "6": "Мастер химии",
    }

    level_id = callback.data.split("_")[1]
    level_name = levels[level_id]

    await state.update_data(
        level_id=level_id,   # для выбора шаблона
        level=level_name    # для вывода в PDF
    )

    await callback.message.answer(
        "Выберите пол ученика:",
        reply_markup=gender_kb
    )
    await state.set_state(CertificateFSM.gender)
    await callback.answer()

# ===== АНГЛИЙСКИЙ =====

# выбор направления
@dp.callback_query(F.data.startswith("eng_"), CertificateFSM.level)
async def english_level_selected(callback, state):

    if callback.data == "eng_abc":
        await state.update_data(level_id="abc")
        await callback.message.answer("Введите максимальное количество баллов:")
        await state.set_state(CertificateFSM.eng_total)

    elif callback.data == "eng_school":
        await state.update_data(level_id="school")
        await callback.message.answer("Какой тест?", reply_markup=eng_school_test_kb)
        await state.set_state(CertificateFSM.eng_test_type)

    elif callback.data == "eng_teens":
        await state.update_data(level_id="teens")
        await callback.message.answer("Укажите общий уровень:", reply_markup=eng_teens_base_kb)
        await state.set_state(CertificateFSM.eng_base_level)

    await callback.answer()


# school → тип теста
@dp.callback_query(F.data.startswith("eng_test_"), CertificateFSM.eng_test_type)
async def eng_school_test_type(callback, state):
    test_type = callback.data.split("_")[2]
    await state.update_data(test_type=test_type)

    await callback.message.answer("Укажите уровень:", reply_markup=eng_school_base_kb)
    await state.set_state(CertificateFSM.eng_base_level)
    await callback.answer()


# выбор base уровня
@dp.callback_query(F.data.startswith("eng_base_"), CertificateFSM.eng_base_level)
async def eng_base(callback, state):
    base = callback.data.replace("eng_base_", "")
    await state.update_data(base_level=base)

    data = await state.get_data()

    # school + umk → баллы
    if data["level_id"] == "school" and data["test_type"] == "umk":
        await callback.message.answer("Введите максимальное количество баллов:")
        await state.set_state(CertificateFSM.eng_total)

    # остальные → skills
    else:
        await callback.message.answer("Listening:", reply_markup=eng_skill_kb)
        await state.set_state(CertificateFSM.eng_listening)

    await callback.answer()


# listening
@dp.callback_query(F.data.startswith("eng_skill_"), CertificateFSM.eng_listening)
async def eng_listening(callback, state):
    await state.update_data(eng_listening=callback.data.replace("eng_skill_", "").upper())
    await callback.message.answer("Reading:", reply_markup=eng_skill_kb)
    await state.set_state(CertificateFSM.eng_reading)
    await callback.answer()


# reading
@dp.callback_query(F.data.startswith("eng_skill_"), CertificateFSM.eng_reading)
async def eng_reading(callback, state):
    await state.update_data(eng_reading=callback.data.replace("eng_skill_", "").upper())
    await callback.message.answer("Speaking:", reply_markup=eng_skill_kb)
    await state.set_state(CertificateFSM.eng_speaking)
    await callback.answer()


# speaking
@dp.callback_query(F.data.startswith("eng_skill_"), CertificateFSM.eng_speaking)
async def eng_speaking(callback, state):
    await state.update_data(eng_speaking=callback.data.replace("eng_skill_", "").upper())
    data = await state.get_data()

    # school + test level → без writing
    if data["level_id"] == "school" and data["test_type"] == "level":
        await callback.message.answer("Выберите пол:", reply_markup=gender_kb)
        await state.set_state(CertificateFSM.gender)
    else:
        await callback.message.answer("Writing:", reply_markup=eng_skill_kb)
        await state.set_state(CertificateFSM.eng_writing)

    await callback.answer()


# writing
@dp.callback_query(F.data.startswith("eng_skill_"), CertificateFSM.eng_writing)
async def eng_writing(callback, state):
    await state.update_data(eng_writing=callback.data.replace("eng_skill_", "").upper())
    await callback.message.answer("Выберите пол:", reply_markup=gender_kb)
    await state.set_state(CertificateFSM.gender)
    await callback.answer()


# баллы
@dp.message(CertificateFSM.eng_total)
async def eng_total(message, state):
    await state.update_data(eng_total=message.text)
    await message.answer("Введите набранные баллы:")
    await state.set_state(CertificateFSM.eng_score)

@dp.message(CertificateFSM.eng_score)
async def eng_score(message, state):
    await state.update_data(eng_score=message.text)
    await message.answer("Выберите пол:", reply_markup=gender_kb)
    await state.set_state(CertificateFSM.gender)

# Педагог
@dp.message(CertificateFSM.teacher)
async def teacher_handler(message: Message, state: FSMContext):
    teacher = message.text.strip()
    await state.update_data(teacher=teacher)

    data = await state.get_data()
    course_name = data["course_name"]

    if course_name in COURSES_WITH_DATES:
        await message.answer("Введите количество академических часов:")
        await state.set_state(CertificateFSM.hours)
    else:
        await message.answer("Введите год выпуска:")
        await state.set_state(CertificateFSM.year)

# Часы
@dp.message(CertificateFSM.hours)
async def hours_handler(message: Message, state: FSMContext):
    await state.update_data(hours=message.text)
    await message.answer("Введите дату начала занятий (например: 01.09.2024):")
    await state.set_state(CertificateFSM.date_start)

# Дата начала
@dp.message(CertificateFSM.date_start)
async def date_start_handler(message: Message, state: FSMContext):
    await state.update_data(date_start=message.text)
    await message.answer("Введите дату окончания занятий (например: 31.05.2025):")
    await state.set_state(CertificateFSM.date_end)

# Дата окончания
@dp.message(CertificateFSM.date_end)
async def date_end_handler(message: Message, state: FSMContext):
    await state.update_data(date_end=message.text)
    await message.answer("Введите год выпуска:")
    await state.set_state(CertificateFSM.year)

   


# Год выпуска — финал (PDF)
@dp.message(CertificateFSM.year)
async def year_handler(message: Message, state: FSMContext):
    print("🔥 year_handler CALLED")

    await state.update_data(year=message.text)
    data = await state.get_data()

    # ---------- имя файла ----------
    student_name = data["student_name"].strip()
    student_name_for_file = "_".join(student_name.split())
    year = data["year"]
    course = data["course_code"]

    os.makedirs("/tmp", exist_ok=True)
    
    prefix_map = {
        "1": "СК",
        "2": "МА",
        "3": "ГП",
        "4": "М",
        "5": "Л",
        "6": "ПШ",
        "7": "ТУ",
        "8": "Х",
        "9": "ГК",
        "10": "А"
    }
    
    prefix = prefix_map.get(course, "CERT")
    filename = f"{prefix}_{student_name_for_file}_{year}.pdf"
    output_path = os.path.join("/tmp", filename)
    # ---------- выбор курса ----------
    course = data["course_code"]

    if course == "1":  # скорочтение
        level = data["level_id"]
        gender = data["gender"]

        cfg = SPEED_READING_MAP[level][gender]

    elif course == "2":  # ментальная арифметика
        level = data["level_id"]
        gender = data["gender"]

        cfg = MENTAL_ARITHMETIC_MAP[level][gender]

    elif course == "3":  # каллиграфия
        level = data["level_id"]
        gender = data["gender"]

        cfg = CALLIGRAPHY_MAP[level][gender]

    elif course == "4":  # математика
        level = data["level_id"]
        gender = data["gender"]

        cfg = MATH_MAP[level][gender]

    elif course == "5":  # логопедия
    
        gender = data["gender"]

        cfg = SPEECH_THERAPY_MAP[gender]

    elif course == "6":  # подготовка к школе
    
        gender = data["gender"]

        cfg = SCHOOL_PREP_MAP[gender]

    elif course == "7":  # таблица умножения
    
        gender = data["gender"]

        cfg = MULTIPLICATION_TABLE_MAP[gender]

    elif course == "8":  # chem
        level = data["level_id"]
        gender = data["gender"]

        cfg = CHEMISTRY_MAP[level][gender]

    elif course == "9":  #  городской клуб
    
        gender = data["gender"]

        cfg = CITY_CLUB_MAP[gender]

    elif course == "10":  # English
        level = data["level_id"]
        gender = data["gender"]

        if level == "abc":
            key = "abc"

        elif level == "school":
            if data["test_type"] == "umk":
                key = "school_umk"
            else:
                if data["base_level"] == "pre_a1":
                    key = "school_pre_a1"
                else:
                    key = "school_full"

        elif level == "teens":
            key = "teens"

        cfg = ENGLISH_MAP[key][gender]

    else:
        cfg = SIMPLE_TEMPLATES[course]
    print("TEMPLATE PATH:", cfg["template"])
    generate_certificate_from_template(
        template_path=cfg["template"],
        output_path=output_path,
        draw_func=cfg.get("draw"),
        data=data
    )

    await message.answer_document(
FSInputFile(output_path),
caption="Ваш сертификат готов 🎓"
)
    # 👇 ВАЖНО
    if course == "1":  # скорочтение
        await message.answer(
            "Хотите сформировать приложение к сертификату?",
            reply_markup=speed_app_kb
        )
        return  # ⛔️ НЕ чистим state

    # 👇 для всех остальных курсов
    await message.answer(
        "Хотите создать ещё один сертификат?",
        reply_markup=start_kb
    )

    await state.clear()


@dp.callback_query(F.data == "speed_app_yes")
async def speed_app_yes(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "Введите цель обучения по курсу скорочтения:"
    )
    await state.set_state(CertificateFSM.goal)
    await callback.answer()
@dp.message(CertificateFSM.goal)
async def goal_handler(message: Message, state: FSMContext):
    await state.update_data(goal=message.text)

    await message.answer("Чтение вслух — ДО:")
    await state.set_state(CertificateFSM.reading_before)
@dp.message(CertificateFSM.reading_before)
async def reading_before(message: Message, state: FSMContext):
    await state.update_data(reading_before=message.text)

    await message.answer("Чтение вслух — ПОСЛЕ:")
    await state.set_state(CertificateFSM.reading_after)


@dp.message(CertificateFSM.reading_after)
async def reading_after(message: Message, state: FSMContext):
    await state.update_data(reading_after=message.text)

    await message.answer("Мнемотехника — ДО (например: 20 из 40):")
    await state.set_state(CertificateFSM.mnemo_before)
@dp.message(CertificateFSM.mnemo_before)
async def mnemo_before(message: Message, state: FSMContext):
    await state.update_data(mnemo_before=message.text)

    await message.answer("Мнемотехника — ПОСЛЕ (например: 20 из 40):")
    await state.set_state(CertificateFSM.mnemo_after)


@dp.message(CertificateFSM.mnemo_after)
async def mnemo_after(message: Message, state: FSMContext):
    await state.update_data(mnemo_after=message.text)

    await message.answer("Зрительная память — ДО (например: 20 из 40):")
    await state.set_state(CertificateFSM.visual_before)
@dp.message(CertificateFSM.visual_before)
async def visual_before(message: Message, state: FSMContext):
    await state.update_data(visual_before=message.text)

    await message.answer("Зрительная память — ПОСЛЕ (например: 20 из 40):")
    await state.set_state(CertificateFSM.visual_after)


@dp.message(CertificateFSM.visual_after)
async def visual_after(message: Message, state: FSMContext):
    await state.update_data(visual_after=message.text)

    await message.answer("Наглядно-образная память — ДО (например: 20 из 40):")
    await state.set_state(CertificateFSM.image_before)
@dp.message(CertificateFSM.image_before)
async def image_before(message: Message, state: FSMContext):
    await state.update_data(image_before=message.text)

    await message.answer("Наглядно-образная память — ПОСЛЕ (например: 20 из 40):")
    await state.set_state(CertificateFSM.image_after)


@dp.message(CertificateFSM.image_after)
async def image_after(message: Message, state: FSMContext):
    await state.update_data(image_after=message.text)

    await message.answer("Динамическая память — ДО (например: 20 из 40):")
    await state.set_state(CertificateFSM.dynamic_before)
@dp.message(CertificateFSM.dynamic_before)
async def dynamic_before(message: Message, state: FSMContext):
    await state.update_data(dynamic_before=message.text)

    await message.answer("Динамическая память — ПОСЛЕ (например: 20 из 40):")
    await state.set_state(CertificateFSM.dynamic_after)



@dp.message(CertificateFSM.dynamic_after)
async def dynamic_after(message: Message, state: FSMContext):
    await state.update_data(dynamic_after=message.text)
    data = await state.get_data()

    level = data["level_id"]  # 1–5
    cfg = SPEED_READING_APPENDIX_MAP[level]

    student_name = data["student_name"].strip()
    student_name_for_file = "_".join(student_name.split())
    year = data["year"]

    os.makedirs("/tmp", exist_ok=True)
    filename = f"СК_Приложение_{student_name_for_file}_{year}.pdf"
    output_path = os.path.join("/tmp", filename)

    generate_certificate_from_template(
        template_path=cfg["template"],
        output_path=output_path,
        draw_func=cfg.get("draw"),
        data=data
    )

    await message.answer_document(
        FSInputFile(output_path),
        caption="Приложение к сертификату готово 📎"
    )

    await message.answer(
        "Хотите создать ещё один сертификат?",
        reply_markup=start_kb
    )

    await state.clear()




@dp.callback_query(F.data == "speed_app_yes")
async def speed_reading_app_start(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    # проверка на всякий случай
    if data.get("course_code") != "1":
        await callback.answer("Приложение доступно только для скорочтения", show_alert=True)
        return

    # ⬇️ ВОТ ТУТ ТВОЙ ВЫДЕЛЕННЫЙ КОД
    level = data["level_id"]
    cfg = SPEED_READING_APPENDIX_MAP[level]

    student_name = data["student_name"].strip()
    student_name_for_file = "_".join(student_name.split())
    year = data["year"]

    filename = f"СК_Приложение_{student_name_for_file}_{year}.pdf"
    output_path = os.path.join("pdf", "output", filename)

    generate_certificate_from_template(
        template_path=cfg["template"],
        output_path=output_path,
        draw_func=cfg.get("draw"),
        data=data
    )

    await callback.message.answer_document(
        FSInputFile(output_path),
        caption="Приложение к сертификату готово 📎"
    )

    await callback.answer()


async def main():
    await dp.start_polling(bot)


# ================= RUN =================

if __name__ == "__main__":
    asyncio.run(main())