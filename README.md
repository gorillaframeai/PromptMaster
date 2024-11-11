# PromptMaster by GorillaFrame

## Author
**GorillaFrame**
Contact: [@GorillaFrame](https://t.me/GorillaFrame)

## About
A tool for processing prompts in text files. The program finds all .txt files in folders and subfolders, reads their content and adds random tags from settings.

## Installation and Launch

1. Make sure Python 3.x is installed
2. Download all project files
3. Create an input folder and put your .txt files there (can be in subfolders)
4. Run the script:
```bash
python process_prompts.py
```
5. Processed files will appear in the output folder with exactly the same folder structure

## Project Structure
```
project/
├── input/                    # Source files
│   ├── folder1/
│   │   └── prompt1.txt
│   └── folder2/
│       └── prompt2.txt
├── output/                   # Processed files
├── config.json              # Prompt settings
└── process_prompts.py       # Main script
```

Example of folder structure preservation:
```
input/
├── animals/
│   ├── cats/
│   │   └── cat1.txt
│   └── dogs/
│       └── dog1.txt
└── people/
    └── person1.txt

Will be processed to:

output/
├── animals/
│   ├── cats/
│   │   └── cat1.txt
│   └── dogs/
│       └── dog1.txt
└── people/
    └── person1.txt
```

## How it works

1. The program searches for all .txt files in the input folder and its subfolders
2. Reads the entire content of each found file (the entire text becomes a prompt)
3. In config.json this text is denoted as [find_file_prompt]
4. Random tags from config.json are added to this text
5. Saves new files to the output folder with exactly the same folder structure as in input

## Important about [find_file_prompt]:

- If [find_file_prompt] is present in structure - the file text will be added to this place in the prompt
- If [find_file_prompt] is absent in structure - the file text will not be used, only tags from config.json will be added

Examples:

1. With file text:
```json
"structure": "[find_file_prompt] [random] [quality] [tags]"
```
Result: `source_file_text rabbit eating grass masterpiece, best quality #Portrait`

2. Without file text:
```json
"structure": "[random] [quality] [tags]"
```
Result: `rabbit eating grass masterpiece, best quality #Portrait`

## Config.json settings

You can add any new tags in square brackets []. Each tag must have a corresponding entry in the settings:

```json
{
    "prompt_settings": {
        "structure": "[find_file_prompt] [random] [quality] [tags] [style] [camera] [lighting] [season] [emotion] [background]",
        "random": "rabbit eating grass@horse riding bicycle@cat sleeping on sofa",
        "quality": "masterpiece, best quality@ultra detailed, best quality",
        "tags": "#Portrait@#Landscape@#Action",
        "style": "oil painting@watercolor@digital art@pencil sketch",
        "camera": "close-up shot@wide angle@bokeh@macro lens",
        "lighting": "natural lighting@studio lighting@dramatic shadows@soft light",
        "season": "spring morning@summer sunset@autumn evening@winter night",
        "emotion": "happy@peaceful@energetic@mysterious",
        "background": "blurred city@nature landscape@abstract patterns@solid color"
    }
}
```

Important points:
- [find_file_prompt] - all text found in source file
- You can add any new tags in [square brackets]
- @ separates variants, one of which will be randomly selected
- Tag order in structure determines order in final prompt
- All tags from structure must have corresponding values in settings

Example results:

Source file input/folder1/prompt.txt:
```
1girl, looking at viewer, smile
```

After processing in output/folder1/prompt.txt:
```
1girl, looking at viewer, smile rabbit eating grass masterpiece, best quality #Portrait oil painting close-up shot natural lighting spring morning happy blurred city
```

Running the program again will create new random combinations from the specified variants.

---

# PromptMaster by GorillaFrame

## Автор
**GorillaFrame**
Контакты: [@GorillaFrame](https://t.me/GorillaFrame)

## О программе
Инструмент для обработки промптов в текстовых файлах. Программа находит все .txt файлы в папках и подпапках, считывает их содержимое и добавляет к нему случайные теги из настроек.

## Установка и запуск

1. Убедитесь что установлен Python 3.x
2. Скачайте все файлы проекта
3. Создайте папку input и положите туда ваши .txt файлы (можно в подпапках)
4. Запустите скрипт:
```bash
python process_prompts.py
```
5. Обработанные файлы появятся в папке output с точно такой же структурой папок

## Структура проекта
```
project/
├── input/                    # Исходные файлы
│   ├── folder1/
│   │   └── prompt1.txt
│   └── folder2/
│       └── prompt2.txt
├── output/                   # Обработанные файлы
├── config.json              # Настройки промптов
└── process_prompts.py       # Основной скрипт
```

Пример сохранения структуры папок:
```
input/
├── animals/
│   ├── cats/
│   │   └── cat1.txt
│   └── dogs/
│       └── dog1.txt
└── people/
    └── person1.txt

Будет обработано в:

output/
├── animals/
│   ├── cats/
│   │   └── cat1.txt
│   └── dogs/
│       └── dog1.txt
└── people/
    └── person1.txt
```

## Как это работает

1. Программа ищет все .txt файлы в папке input и её подпапках
2. Считывает содержимое каждого найденного файла полностью (весь текст становится промптом)
3. В config.json этот текст обозначается как [find_file_prompt]
4. К этому тексту добавляются случайные теги из config.json
5. Сохраняет новые файлы в папку output с точно такой же структурой папок, как в input

## Важно про [find_file_prompt]:

- Если [find_file_prompt] есть в structure - текст из файла будет добавлен в это место промпта
- Если [find_file_prompt] отсутствует в structure - текст из файла не будет использован, а будут добавлены только теги из config.json

Примеры:

1. С использованием текста из файла:
```json
"structure": "[find_file_prompt] [random] [quality] [tags]"
```
Результат: `исходный_текст_файла rabbit eating grass masterpiece, best quality #Portrait`

2. Без использования текста из файла:
```json
"structure": "[random] [quality] [tags]"
```
Результат: `rabbit eating grass masterpiece, best quality #Portrait`

## Настройка config.json

Вы можете добавлять любые новые теги в квадратных скобках []. Каждый такой тег должен иметь соответствующую запись в настройках:

```json
{
    "prompt_settings": {
        "structure": "[find_file_prompt] [random] [quality] [tags] [style] [camera] [lighting] [season] [emotion] [background]",
        "random": "rabbit eating grass@horse riding bicycle@cat sleeping on sofa",
        "quality": "masterpiece, best quality@ultra detailed, best quality",
        "tags": "#Portrait@#Landscape@#Action",
        "style": "oil painting@watercolor@digital art@pencil sketch",
        "camera": "close-up shot@wide angle@bokeh@macro lens",
        "lighting": "natural lighting@studio lighting@dramatic shadows@soft light",
        "season": "spring morning@summer sunset@autumn evening@winter night",
        "emotion": "happy@peaceful@energetic@mysterious",
        "background": "blurred city@nature landscape@abstract patterns@solid color"
    }
}
```

Важные моменты:
- [find_file_prompt] - весь текст, который был найден в исходном файле
- Можно добавлять любые новые теги в [квадратных скобках]
- @ разделяет варианты, один из которых будет выбран случайным образом
- Порядок тегов в structure определяет порядок в финальном промпте
- Все теги из structure должны иметь соответствующие значения в настройках

Примеры результатов:

Исходный файл input/folder1/prompt.txt:
```
1girl, looking at viewer, smile
```

После обработки в output/folder1/prompt.txt:
```
1girl, looking at viewer, smile rabbit eating grass masterpiece, best quality #Portrait oil painting close-up shot natural lighting spring morning happy blurred city
```

При повторном запуске программы будут созданы новые случайные комбинации из указанных вариантов.