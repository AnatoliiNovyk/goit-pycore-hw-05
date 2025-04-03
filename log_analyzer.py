import re
import sys
from typing import Dict, List, Tuple

def parse_log_line(line: str) -> Dict[str, str]:
    """Парсить рядок логу та повертає словник з компонентами."""
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.*)"
    match = re.match(pattern, line)
    if match:
        return {
            "timestamp": match.group(1),
            "level": match.group(2),
            "message": match.group(3).strip(),
        }
    return {}

def load_logs(file_path: str) -> List[Dict[str, str]]:
    """Завантажує логи з файлу."""
    logs = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                log_entry = parse_log_line(line.strip())
                if log_entry:
                    logs.append(log_entry)
    except FileNotFoundError:
        print(f"Помилка: Файл не знайдено за шляхом: {file_path}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    """Фільтрує логи за рівнем."""
    return [log for log in logs if log.get("level") == level.upper()]

def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """Підраховує кількість записів за рівнем логування."""
    counts = {}
    for log in logs:
        level = log.get("level")
        if level:
            counts[level] = counts.get(level, 0) + 1
    return counts

def display_log_counts(counts: Dict[str, int]):
    """Форматує та виводить результати підрахунку логів."""
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16}| {count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Використання: python log_analyzer.py <шлях_до_файлу_логу> [рівень_логування]")
        sys.exit(1)

    log_file_path = sys.argv[1]
    logs = load_logs(log_file_path)
    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)

    if len(sys.argv) > 2:
        log_level_filter = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, log_level_filter)
        print(f"\nДеталі логів для рівня '{log_level_filter.upper()}':")
        for log in filtered_logs:
            print(f"{log['timestamp']} - {log['message']}")
