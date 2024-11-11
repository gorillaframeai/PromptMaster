import os
import json
import random
import shutil

def load_config():
    try:
        with open('config.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Ошибка при чтении config.json: {str(e)}")
        return None

def generate_prompt(config, original_text):
    prompt_settings = config['prompt_settings']
    structure = prompt_settings['structure']
    
    def get_random_value(key):
        value = prompt_settings.get(key, '')
        if '@' in value:
            return random.choice(value.split('@'))
        return value
    
    result = structure
    # Если текст пустой, убираем [find_file_prompt] из structure
    if not original_text:
        result = result.replace('[find_file_prompt], ', '')
        result = result.replace('[find_file_prompt]', '')
    
    for key in prompt_settings:
        if key != 'structure' and key != 'copy_images':
            placeholder = f'[{key}]'
            if placeholder in result:
                if key == 'find_file_prompt' and original_text:
                    result = result.replace(placeholder, original_text)
                else:
                    result = result.replace(placeholder, get_random_value(key))
    
    return result

def process_file(source_path, dest_path, config):
    try:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        
        base_name = os.path.splitext(source_path)[0]
        txt_path = base_name + '.txt'
        
        # Если это txt файл - обрабатываем его
        if source_path.endswith('.txt'):
            with open(source_path, 'r', encoding='utf-8') as file:
                original_content = file.read().strip()
            
            prompt = generate_prompt(config, original_content)
            
            with open(dest_path, 'w', encoding='utf-8') as file:
                file.write(prompt)
            
            print(f"Обработан файл: {source_path} -> {dest_path}")
            print(f"Новый промпт: {prompt}")
            
        # Если это изображение
        elif source_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Если нет txt файла, создаем его
            if not os.path.exists(txt_path):
                prompt = generate_prompt(config, "")
                txt_dest_path = os.path.splitext(dest_path)[0] + '.txt'
                
                with open(txt_dest_path, 'w', encoding='utf-8') as file:
                    file.write(prompt)
                
                print(f"Создан промпт: {txt_dest_path}")
                print(f"Новый промпт: {prompt}")
            
            # Копируем изображение если включено
            if config['prompt_settings'].get('copy_images', True):
                shutil.copy2(source_path, dest_path)
                print(f"Скопирован файл: {source_path} -> {dest_path}")
        
        return True, None
    except Exception as e:
        error_msg = f"Ошибка при обработке файла {source_path}: {str(e)}"
        print(error_msg)
        return False, error_msg

def process_directory(source_dir, output_dir, config):
    processed_files = 0
    errors = []
    
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(('.txt', '.png', '.jpg', '.jpeg')):
                rel_path = os.path.relpath(root, source_dir)
                source_path = os.path.join(root, file)
                dest_path = os.path.join(output_dir, rel_path, file)
                success, error = process_file(source_path, dest_path, config)
                if success:
                    processed_files += 1
                if error:
                    errors.append(error)
    
    return processed_files, errors

if __name__ == "__main__":
    print("""
╔═══════════════════════════════════════╗
║      PromptMaster by GorillaFrame     ║
║              Version 1.0.0            ║
╚═══════════════════════════════════════╝
    """)
    
    config = load_config()
    if not config:
        print("Не удалось загрузить конфигурацию. Завершение работы.")
        exit(1)

    source_directory = "input"
    output_directory = "output"
    
    os.makedirs(output_directory, exist_ok=True)
    processed_files, errors = process_directory(source_directory, output_directory, config)
    
    print("\n" + "="*50)
    print(f"Обработка завершена!")
    print(f"Всего обработано файлов: {processed_files}")
    
    if errors:
        print("\nБыли обнаружены ошибки:")
        for error in errors:
            print(f"- {error}")
    else:
        print("Ошибок не обнаружено")
    print("="*50)