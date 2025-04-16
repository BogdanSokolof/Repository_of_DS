"""РРеализация ьинапнргр поиска"""

def search_iterative(self, list, item):
    # low and high uграницы списка в котором выполняется поиск
    low = 0
    high = len(list) - 1

    # Пока поиск не сократится до одного элемента ...
    while low <= high:
      # ... Ищем середину
      mid = (low + high) // 2
      guess = list[mid]
      # Значение найдено
      if guess == item:
        return mid
      # Если значение слишком велико.
      if guess > item:
        high = mid - 1
      # Если значение слишком мало.
      else:
        low = mid + 1