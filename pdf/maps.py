from pathlib import Path

from pdf.layouts.speed_reading.level_1 import draw_speed_reading_level_1
from pdf.layouts.speed_reading.level_2 import draw_speed_reading_level_2
from pdf.layouts.speed_reading.level_3 import draw_speed_reading_level_3
from pdf.layouts.speed_reading.level_4 import draw_speed_reading_level_4
from pdf.layouts.speed_reading.level_5 import draw_speed_reading_level_5


from pdf.layouts.mental_arithmetic.level_1 import draw_mental_level_1

BASE_DIR = Path(__file__).resolve().parent
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SIMPLE_TEMPLATES = {
    "Математика": "pdf/templates/math.pdf",
    "Английский язык": "pdf/templates/english.pdf",
    "Химия": "pdf/templates/chemistry.pdf",
    "Городской клуб": "pdf/templates/city_club.pdf",
}

COURSE_MAP = {
    "1": {  # Скорочтение
        "type": "speed_reading"
    },
    "2": {  # Ментальная арифметика
        "type": "mental_arithmetic"
    },
    "3": {  
        "type": "calligraphy"
    },
    "4": {  
        "type": "math"
    },
    "5": {  
        "type": "chemistry"
    },
    "6": {  
        "type": "city_club"
    },
    "7": {  
        "type": "english"
    }
}



SPEED_READING_MAP = {
    "1": {
        "boy": {
            "template": BASE_DIR /"pdf/templates/speed_reading/level_1/boy.pdf",
            "draw": draw_speed_reading_level_1,
        },
        "girl": {
            "template": BASE_DIR / "pdf/templates/speed_reading/level_1/girl.pdf",
            "draw": draw_speed_reading_level_1,
        },
    },
    "2": {
        "boy": {
            "template": BASE_DIR / "pdf/templates/speed_reading/level_2/boy.pdf",
            "draw": draw_speed_reading_level_2,
        },
        "girl": {
            "template": BASE_DIR / "pdf/templates/speed_reading/level_2/girl.pdf",
            "draw": draw_speed_reading_level_2,
        },
    },
    "3": {
        "boy": {
            "template": BASE_DIR / "pdf/templates/speed_reading/level_3/boy.pdf",
            "draw": draw_speed_reading_level_3,
        },
        "girl": {
            "template": BASE_DIR / "pdf/templates/speed_reading/level_3/girl.pdf",
            "draw": draw_speed_reading_level_3,
        },
    },
    "4": {
        "boy": {
            "template": BASE_DIR / "pdf/templates/speed_reading/level_4/boy.pdf",
            "draw": draw_speed_reading_level_4,
        },
        "girl": {
            "template": BASE_DIR / "pdf/templates/speed_reading/level_4/girl.pdf",
            "draw": draw_speed_reading_level_4,
        },
    },
    "5": {
        "boy": {
            "template": BASE_DIR / "pdf/templates/speed_reading/level_5/boy.pdf",
            "draw": draw_speed_reading_level_5,
        },
        "girl": {
            "template": BASE_DIR / "pdf/templates/speed_reading/level_5/girl.pdf",
            "draw": draw_speed_reading_level_5,
        },
    }
}


from pdf.layouts.mental_arithmetic.level_1 import draw_mental_level_1
from pdf.layouts.mental_arithmetic.level_2 import draw_mental_level_2
from pdf.layouts.mental_arithmetic.level_3 import draw_mental_level_3
from pdf.layouts.mental_arithmetic.level_4 import draw_mental_level_4

MENTAL_ARITHMETIC_MAP = {
    "1": {
        "boy": {
            "template": BASE_DIR / "pdf" / "templates" / "mental_arithmetic" / "level_1" / "boy.pdf",
            "draw": draw_mental_level_1,
        },
        "girl": {
            "template": BASE_DIR / "pdf" / "templates" / "mental_arithmetic" / "level_1" / "girl.pdf",
            "draw": draw_mental_level_1
        }
    },
    "2": {
        "boy": {
            "template": BASE_DIR / "pdf" / "templates" / "mental_arithmetic" / "level_2" / "boy.pdf",
            "draw": draw_mental_level_2,
        },
        "girl": {
            "template": BASE_DIR / "pdf" / "templates" / "mental_arithmetic" / "level_2" / "girl.pdf",
            "draw": draw_mental_level_2
        }
    },
    "3": {
        "boy": {
            "template": BASE_DIR / "pdf" / "templates" / "mental_arithmetic" / "level_3" / "boy.pdf",
            "draw": draw_mental_level_3,
        },
        "girl": {
            "template": BASE_DIR / "pdf" / "templates" / "mental_arithmetic" / "level_3" / "girl.pdf",
            "draw": draw_mental_level_3
        }
    },
    "4": {
        "boy": {
            "template": BASE_DIR / "pdf" / "templates" / "mental_arithmetic" / "level_4" / "boy.pdf",
            "draw": draw_mental_level_4,
        },
        "girl": {
            "template": BASE_DIR / "pdf" / "templates" / "mental_arithmetic" / "level_4" / "girl.pdf",
            "draw": draw_mental_level_4
        }
    }
}



from pdf.layouts.calligraphy.level_1 import draw_calligraphy_level_1
from pdf.layouts.calligraphy.level_2 import draw_calligraphy_level_2
from pdf.layouts.calligraphy.level_3 import draw_calligraphy_level_3

CALLIGRAPHY_MAP = {
    "1": {
        "boy": {
            "template": BASE_DIR / "pdf/templates/calligraphy/level_1/boy.pdf",
            "draw": draw_calligraphy_level_1
        },
        "girl": {
            "template": BASE_DIR / "pdf/templates/calligraphy/level_1/girl.pdf",
            "draw": draw_calligraphy_level_1
        }
    },
    "2": {
        "boy": {
            "template": BASE_DIR / "pdf/templates/calligraphy/level_2/boy.pdf",
            "draw": draw_calligraphy_level_2
        },
        "girl": {
            "template": BASE_DIR / "pdf/templates/calligraphy/level_2/girl.pdf",
            "draw": draw_calligraphy_level_2
        }
    },
    "3": {
        "boy": {
            "template": BASE_DIR / "pdf/templates/calligraphy/level_3/boy.pdf",
            "draw": draw_calligraphy_level_3
        },
        "girl": {
            "template": BASE_DIR / "pdf/templates/calligraphy/level_3/girl.pdf",
            "draw": draw_calligraphy_level_3
        }
    }
}










from pdf.layouts.math.level_1 import draw_math_level_1
from pdf.layouts.math.level_2 import draw_math_level_2
from pdf.layouts.math.level_3 import draw_math_level_3

MATH_MAP = {
    "1": {
        "boy": {
            "template": BASE_DIR / "pdf/templates/math/level_1/boy.pdf",
            "draw": draw_math_level_1
        },
        "girl": {
            "template": BASE_DIR / "pdf/templates/math/level_1/girl.pdf",
            "draw": draw_math_level_1
        }
    },
    "2": {
        "boy": {
            "template": BASE_DIR / "pdf/templates/math/level_2/boy.pdf",
            "draw": draw_math_level_2
        },
        "girl": {
            "template": BASE_DIR / "pdf/templates/math/level_2/girl.pdf",
            "draw": draw_math_level_2
        }
    },
    "3": {
        "boy": {
            "template": BASE_DIR / "pdf/templates/math/level_3/boy.pdf",
            "draw": draw_math_level_3
        },
        "girl": {
            "template": BASE_DIR / "pdf/templates/math/level_3/girl.pdf",
            "draw": draw_math_level_3
        }
    }
}

from pdf.layouts.speech_therapy.base import draw_speech_therapy

SPEECH_THERAPY_MAP = {
    "boy": {
        "template": BASE_DIR /"pdf/templates/speech/boy.pdf",
        "draw": draw_speech_therapy
    },
    "girl": {
        "template": BASE_DIR /"pdf/templates/speech/girl.pdf",
        "draw": draw_speech_therapy
    }
}


from pdf.layouts.school_prep.base import draw_school_prep

SCHOOL_PREP_MAP = {
    "boy": {
        "template": BASE_DIR /"pdf/templates/school_prep/boy.pdf",
        "draw": draw_school_prep
    },
    "girl": {
        "template": BASE_DIR /"pdf/templates/school_prep/girl.pdf",
        "draw": draw_school_prep
    }
}

from pdf.layouts.multiplication.base import draw_multiplication

MULTIPLICATION_TABLE_MAP = {
    "boy": {
        "template": BASE_DIR /"pdf/templates/multiplication/boy.pdf",
        "draw": draw_multiplication
    },
    "girl": {
        "template": BASE_DIR /"pdf/templates/multiplication/girl.pdf",
        "draw": draw_multiplication
    }
}



from pdf.layouts.chemistry.level_1 import draw_chemistry_level_1
from pdf.layouts.chemistry.level_2 import draw_chemistry_level_2
from pdf.layouts.chemistry.level_3 import draw_chemistry_level_3
from pdf.layouts.chemistry.level_4 import draw_chemistry_level_4
from pdf.layouts.chemistry.level_5 import draw_chemistry_level_5
from pdf.layouts.chemistry.level_6 import draw_chemistry_level_6


CHEMISTRY_MAP = {
    "1": {
        "boy": {
            "template":  BASE_DIR /"pdf/templates/chemistry/level_1/boy.pdf",
            "draw": draw_chemistry_level_1
        },
        "girl": {
            "template": BASE_DIR /"pdf/templates/chemistry/level_1/girl.pdf",
            "draw": draw_chemistry_level_1
        }
    },
    "2": {
        "boy": {
            "template": BASE_DIR /"pdf/templates/chemistry/level_2/boy.pdf",
            "draw": draw_chemistry_level_2
        },
        "girl": {
            "template": BASE_DIR /"pdf/templates/chemistry/level_2/girl.pdf",
            "draw": draw_chemistry_level_2
        }
    },
    "3": {
        "boy": {
            "template": BASE_DIR /"pdf/templates/chemistry/level_3/boy.pdf",
            "draw": draw_chemistry_level_3
        },
        "girl": {
            "template": BASE_DIR /"pdf/templates/chemistry/level_3/girl.pdf",
            "draw": draw_chemistry_level_3
        }
    },
    "4": {
        "boy": {
            "template": BASE_DIR /"pdf/templates/chemistry/level_4/boy.pdf",
            "draw": draw_chemistry_level_4
        },
        "girl": {
            "template": BASE_DIR /"pdf/templates/chemistry/level_4/girl.pdf",
            "draw": draw_chemistry_level_4
        }
    },
    "5": {
        "boy": {
            "template": BASE_DIR /"pdf/templates/chemistry/level_5/boy.pdf",
            "draw": draw_chemistry_level_5
        },
        "girl": {
            "template": BASE_DIR /"pdf/templates/chemistry/level_5/girl.pdf",
            "draw": draw_chemistry_level_5
        }
    },
    "6": {
        "boy": {
            "template": BASE_DIR /"pdf/templates/chemistry/level_6/boy.pdf",
            "draw": draw_chemistry_level_6
        },
        "girl": {
            "template": BASE_DIR /"pdf/templates/chemistry/level_6/girl.pdf",
            "draw": draw_chemistry_level_6
        }
    }
}


from pdf.layouts.speed_reading.level_1 import draw_speed_reading_appendix_level_1
from pdf.layouts.speed_reading.level_2 import draw_speed_reading_appendix_level_2
from pdf.layouts.speed_reading.level_3 import draw_speed_reading_appendix_level_3
from pdf.layouts.speed_reading.level_4 import draw_speed_reading_appendix_level_4
from pdf.layouts.speed_reading.level_5 import draw_speed_reading_appendix_level_5

SPEED_READING_APPENDIX_MAP = {
    "1": {
        "template": BASE_DIR /"pdf/templates/speed_reading/level_1/appendix.pdf",
        "draw": draw_speed_reading_appendix_level_1
    },
    "2": {
        "template": BASE_DIR /"pdf/templates/speed_reading/level_2/appendix.pdf",
        "draw": draw_speed_reading_appendix_level_2
    },
    "3": {
        "template": BASE_DIR /"pdf/templates/speed_reading/level_3/appendix.pdf",
        "draw": draw_speed_reading_appendix_level_3
    },
    "4": {
        "template": BASE_DIR /"pdf/templates/speed_reading/level_4/appendix.pdf",
        "draw": draw_speed_reading_appendix_level_4
    },
    "5": {
        "template": BASE_DIR /"pdf/templates/speed_reading/level_5/appendix.pdf",
        "draw": draw_speed_reading_appendix_level_5
    },
}


from pdf.layouts.city_club.base import draw_city_club

CITY_CLUB_MAP = {
    "boy": {
        "template": BASE_DIR /"pdf/templates/city_club/boy.pdf",
        "draw": draw_city_club
    },
    "girl": {
        "template": BASE_DIR /"pdf/templates/city_club/girl.pdf",
        "draw": draw_city_club
    }
}


from pdf.layouts.english.level_1 import draw_english_level_1
from pdf.layouts.english.level_2umk import draw_english_level_2
from pdf.layouts.english.level_2pre import draw_english_level_22
from pdf.layouts.english.level_3 import draw_english_level_3

ENGLISH_MAP = {
    
    "abc": {
        "boy": {
            "template": BASE_DIR /"pdf/templates/english/level_1/boy.pdf",
            "draw": draw_english_level_1
        },
        "girl": {
            "template": BASE_DIR /"pdf/templates/english/level_1/girl.pdf",
            "draw": draw_english_level_1
        }
    },
    "school_umk":{
        "boy": {
            "template": BASE_DIR /"pdf/templates/english/level_2umk/boy.pdf",
            "draw": draw_english_level_2
        },
        "girl": {
            "template": BASE_DIR /"pdf/templates/english/level_2umk/girl.pdf",
            "draw": draw_english_level_2
        }
    },
    "school_pre_a1":{
        "boy": {
            "template": BASE_DIR /"pdf/templates/english/level_2pre/boy.pdf",
            "draw": draw_english_level_22
        },
        "girl": {
            "template": BASE_DIR /"pdf/templates/english/level_2pre/girl.pdf",
            "draw": draw_english_level_22
        }
    },
    "school_full":{
        "boy": {
            "template": BASE_DIR /"pdf/templates/english/level_1/boy.pdf",
            "draw": draw_english_level_1
        },
        "girl": {
            "template": BASE_DIR /"pdf/templates/english/level_1/girl.pdf",
            "draw": draw_english_level_1
        }
    },
    "teens": {
        "boy": {
            "template": BASE_DIR /"pdf/templates/english/level_3/boy.pdf",
            "draw": draw_english_level_3
        },
        "girl": {
            "template": BASE_DIR /"pdf/templates/english/level_3/girl.pdf",
            "draw": draw_english_level_3
        }
    }
}













COURSE_MAP = {
    "speed_reading": SPEED_READING_MAP,
    "mental_arithmetic": MENTAL_ARITHMETIC_MAP,
}