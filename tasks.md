# Задачи

## 1. Вводная лекция

### 1. Основы git и bash

1. Упражения с git на новом репозитории

- Создать локальный пустой репозиторий
- Добавить файл, сделать коммит.
- Откатиться туда и обратно.

2. Упражнения с git на готовом репозитории

- Сделать форк основного репозитория
- Вытянуть локально репозиторий
- Добавить пустой файл

### 2. Основы Python

1. **(1 балл)** Рукопожатие — один из способов приветствия, который нам достался из античности. Студенты Политеха тоже здороваются рукопожатием. Обычно парни. Сколько раз жмут руку друг другу парни при встрече, если каждый здоровается с каждым?  Напишите функцию, которая вычисляет это значение.
2. **(1 балл)** На чемпионате The Internetional  в следующем году будет участвовать много команд. Сколько существует вариантов распределить первые три места? А все места? Напишите функцию, которая вычисляет эти значения.
3. **(1 балл)** Вы разработчик в компании, которая выполняет заказ для государственной разведывательной службы. Сейчас Ваш отдел работает над анализом социологических данных по одной бедной азиатской стране. Недавно там приняли новую программу поддержки рождаемости. Правительство дает за рождение мальчика огромную сумму денег. Но больше одного мальчика иметь нельзя. При этом количество детей в семье неограниченно. Руководство попросило Вас составить прогноз и понять какое будет распределение мужчин и женщин в этой азиатской стране в будущем, если каждая семья будет рожать до тех пор, пока не родится мальчик. Модель должна быть простой. Напишите программу, которая моделирует рождаемость в этой стране. Можно ли решить задачу аналитически?
4. **(1 балл)** Вы разработчик игр и разбираетесь с жалобами игроков. Многие ругаются, что герои часто застревают в текстурах. Оказалось, что функция, которая проверяет пересечение фигуры героя со стенами написана с ошибкой. Надо переписать. Напишите функцию, которая проверяет пересекаются ли два прямоугольника. Они заданы двумя точками диагонали, стороны параллельны осям декартовой системы координат. Можно ли переписать программу так, чтобы она выдавала координаты пересечения?
5. **(1 балл)** Вы разработчик игр и работаете над новой фичей (функцией) для игры. Сейчас надо реализовать логику работы сражений в игре. Во время сражения игрока с противником каждый наносит удар. У кого сила удара больше, тот и нанес урон. Противники в игре — боты. За них никто не играет. Поэтому силу удара надо формировать случайно. Напишите функцию, которая выдает псевдослучайное число силы удара. Сделайте это с помощью  линейного конгруэнтного метода <img src="https://render.githubusercontent.com/render/math?math=x_{n%2B1} =(a x_n%2Bc)\mod m">, где <img src="https://render.githubusercontent.com/render/math?math=x_0&mode=inline"> — seed.
6. **(1 балл)** Вы разработчик программ для банка. Руководство попросило Вас написать программу для печати квитанций и чеков. На чеках надо рядом с суммой выводить ее значение текстом. Это нужно, чтобы сложнее было подделать бумаги. Одну цифру легко исправить, а если еще и слово переписать, то сложнее. Напишите программу, которая выводит текстовую строку для целого числа.
7. **(5 баллов)** Вы автор программы №1.2.2. Вашу программу захотела купить компания 1xbet, чтобы анализировать ставки. Но они хотят, чтобы программа работала быстрее с большими числами. Можно ли ускорить программу? Математики из компании утверждают, что можно использовать для этого разложение на простые множители. <details><summary>ℹ️ Подсказка</summary>Тут поможет решето Эратосфена?</details>
8. **(1 балл)** Вы разработчик игр и ваш коллега написал только что функцию проверки на пересечение двух прямоугольников, которые заданы двумя точками диагонали. Надо проверить не сделал ли он ошибок. Напишите проверки (тесты). Для этого используйте конструкцию `assert`.
9. **(5 баллов)** Вы разработчик игр и работаете над новой фичей (функцией) для игры. Сейчас надо реализовать логику работы сражений в игре. Во время сражения игрока с противником каждый наносит удар. У кого сила удара больше, тот и нанес урон. Напишите функцию, которая реализует эту логику. К сожалению, игра для старой слабой платформы, где нет аппаратной поддержки операций сравнения. Поэтому надо написать код без них. Разработчики аппаратуры подсказали, что можно использовать бинарное представление чисел.

## 2. Алгоритмы и структуры данных. Начало

### 1. Алгоритмы поиска

1. **(2 балла)** В системе регистрации сайта был сбой и в списке идентификаторов пользователей есть повторяющиеся идентификаторы. Напишите функцию, которая проверяет есть ли повторы в списке. Попробуйте найти решение за квазилинейное время. <details><summary>ℹ️ Подсказка</summary>Что будет, если сначала отсортировать?</details>
2. **(5 баллов)** В системе регистрации сайта продолжают происходить ошибки, руководство просит ускорить систему поиска повторов из задачи №2.1.1. Попробуйте ускорить алгоритм до линейного времени. В каком случае это невозможно? <details><summary>ℹ️ Подсказка</summary>А что, если мы используем идентификаторы как индексы?</details>
3. **(3 балла)** В системе регистрации сайта продолжают появлятся дубли идентификаторов пользователей. Руководство решило, что это не баг, а фича. Для удобства список идентификаторов теперь хранят в упорядоченном виде. Напишите функцию, которая возвращает индекс искомого идентификатора. Если их несколько, то первого.
4. **(2 балла)** В репозитории курса есть пакет с некоторыми примерами алгоритмов поиска. С помощью функции `time` из одноименного пакета замерьте время поиска на списках разной длины. Какой алгоритм самый быстрый? Будет ли работать быстрее бинарный поиск, если предварительно вычислять верхнюю границу списка (см. экспоненциальный поиск)?
5. **(3 балла)** Вы разработчик компании, которая производит гиперзвуковые ракеты. В новую модель будут ставить слабый, но надежный чип. В расчетах траектории ракеты используется квадратный корень. Но готовую библиотечную реализацию квадратного корня использовать нельзя, так как чип слабый. Напишите функцию, которая вычисляет квадратный корень вещественного числа с помощью поиска.
6. **(3 балла)** Вы разработчик компании, которая производит гиперзвуковые ракеты. Ваше решение в задаче №2.1.5 понравилось руководству и Вас попросили переписать функцию бинарного поиска так, чтобы она использовала только сложение и вычитание.<details><summary>ℹ️ Подсказка</summary>Может быть тут можно использовать фибоначчиев поиск?</details>
7. **(4 балла)** Вы работаете в компании, которая автоматизирует работу архивов. Руководство попросило Вас разработать программу для поиска данных на старых магнитных лентах, на которых информация упорядочена. Аппарат для чтения быстро проворачивает ленту вперед, но очень медленно назад. Бинарный поиск будет здесь неэффективен, поэтому Вы решили остановиться на линейном. Но можно ли его ускорить, если шагать через несколько элементов сразу? Но тогда какой оптимальный размер шага? Попробуйте вывести размер шага аналитически. Напишите функцию, которая ищет в упрорядоченной последовательности число с помощью этого метода.<details><summary>ℹ️ Подсказка</summary>Почему корень из длины — это эффективный размер шага?</details>
8. **(3 балла, AirBNB)** Перепишите программу №2.1.3 так, чтобы она возвращала всегда два индекса: первого и последнего вхождения искомого символа. Напишите тесты.

## 3. Проектирование алгоритмов

1. **(3 балла)** Вы пришли на собеседование в Google и Вас попросили отсортировать случайную последовательность целых чисел пирамидальной сортировкой. Но вы не знаете как написать код пирамиды. Вам разрешили использовать стандартный модуль `heapq`. Напишите программу сортировки. Протестируйте ее с помощью asserts.
2. **(3 балла)** Вы участник космической программы по колонизации других планет. Сейчас вы находитесь далеко в звездной системе, где вокруг звезды крутятся 3 планеты с периодом `l`, `m` и `k` земных часов. Вы исследуете ближайшую к звезде планету. Периодически вам надо отправлять отчеты на Землю, но ваш передатчик слабый. Поэтому надо использовать ретрансляторы на соседних планетах. Технически это возможно сделать во время противостояния этих трех планет, то есть когда планеты выстроены в одну линию. Напишите программу, которая вычисляет как часто вы можете отправлять отчеты на Землю. Напишите тесты на asserts. <details><summary>ℹ️ Подсказка</summary>Можно ли свести задачу к решению через алгоритм Евклида?</details>
3. **(3 балла)** Вы наблюдатель на выборах. Ваши коллеги сообщили, что в избирательную урну недобросовестные граждане вбросили один фальшивый бюллетень. Он сделан из менее плотной дешевой бумаги, поэтому найти его легко, но бюллетеней много. Под рукой у вас есть рычажные весы. Сколько надо взвешиваний, чтобы найти фальшивый бюллетень? Решите задачу аналитически. <details><summary>ℹ️ Подсказка</summary>А что, если использовать метод «Разделяй и властвуй»?</details>
4. **(3 балла)** Вы все еще на собеседовании в Google. Вас попросили переписать программу №3.1 используя сортировку выбором и показать, что она медленнее пирамидальной. Напишите программу, которая это показывает.
5. **(5 балла)** Вы один из немногих выживших в постапокалиптическом мире. Во время очередного рейда в опустошенный город вы нашли экзотический механический компьютер. К сожалению, вы обнаружили, что из арифметических операций он умеет только складывать, вычитать, умножать на 2 и делить на 2 целые числа. Но чтобы им пользоваться повседневно надо уметь умножать любые целые числа. Как это можно сделать на таком компьютере эффективно? Напишите функцию, которая выполняет умножение двух числе с использованием только `+`, `-`, `<<` (умножение на 2) и `>>` (деление на 2). <details><summary>ℹ️ Подсказка</summary>А что, если использовать метод «Уменьшай и властвуй»?</details>
6. **(3 балла)** Вы разработчик в компании, которая разрабатывает систему автоматизации для выборов. Выяснилось, что основные проблемы связаны не с самим голосованием, а с подсчетом. Видимо из-за человеческого фактора не удается точно посчитать результат. Поэтому решили автоматизировать этот процесс. Ваши коллеги реализовали аппаратную систему, которая распознает по бюллетеню кому был отдан голос. На выходе получается список голосов. Вам необходимо написать программу, которая определяет по этому списку победителя голосования. <details><summary>ℹ️ Подсказка</summary>Будет ли быстрее, если список как-то сначала преобразовать?</details>

## 4. АТД с линейным порядком

### 1. Списки и строки

1. **(4 балла)** Палиндром — это слово, которое читается одинаково слева направо и справа налево (например, ротор). Напишите функцию, которая проверяет является ли слово палиндромом. Напишите тесты.
2. **(6 балла, Yandex)** Перепишите функцию из №4.1.1 так, чтобы она проверяла на палиндромом строки. При этом проверяются только буквы и цифры, остальные символы надо пропускать. Напишите тесты.
3. **(8 баллов, Twitter)** Перепишите функцию из №4.1.1 так, чтобы она находила подстроку максимальной длины, которая является палиндромом. Напишите тесты.
4. **(10 баллов, Microsoft)** Вы работаете в компании, которая разрабатывает передатчики, которые общаются друг с другом с помощью специального протокола. Протокол устроен таким образом, что в принятом сообщении не может быть рядом стоящих одинаковых символов. И если есть дубли, то сообщение принято с ошибкой. Но не все потеряно, можно найти максимальную подпоследовательность без повторов. Ваша задача — написать функцию проверки принятого сообщения, которая возвращает длину наибольшей подстроки без повторов за линейное время. Напишите тесты.
5. **(4 балла, Uber)** Вы работаете в компании, которая разрабатывает новый компилятор для языка Си. Вам поручили реализовать проверку синтаксиса программ. Вы решили начать с проверки расстановки скобок. Напишите функцию, которая проверяет баланс скобок в строке. Возможные символы скобок: `'(', ')', '{', '}', '[' и ']'`. Напишите тесты.

### 2. Связный список

1. **(4 балла)** Реализуйте односвязный список и напишите тесты.
2. **(4 балла, Google)** Напишите функцию, которая переворачивает связный список. Напишите тесты.
3. **(15 баллов)** Напишите адресную книгу на skip-списке. Напишите тесты.
4. **(10 баллов, Microsoft)** Аппаратная поддержка арифметических операций ограничены разраядностью компьютера. Это можно обойти с помощью программной реализации длинной арифметики. Реализуйте длинную арифметику целых чисел на связном списке. Напишите операцию сложения.  Напишите тесты.
5. **(12 баллов)** Дополните решение 4.2.4 операцией умножения. Напишите тесты.<details><summary>ℹ️ Подсказка</summary>Будет ли быстрее, если использовть алгоритм Карацубы?</details>
6. **(8 баллов, Twitter)** Вы устроились в новую компанию, где бывший сотрудник не дописал решение задачи. Надо было реализовать стек, у которого все команды работают за константное время. Закончите решение.
```python
class MaxStack:
  def __init__(self):
    pass

  def push(self, val):
    pass

  def pop(self):
    pass

  def max(self):
    pass
```

## 5. АТД: словарь и множество

### 1. Хэширование и хэш-таблица

1. **(5 баллов)** Вы разрабатывете текстовый редактор. Руководство попросило реализовать новую фичу: поиск в тексте. Вы знаете два подхода к решению задачи и  решили написать оба, чтобы выбрать лучший. Напишите две реализации функции поиска подстроки в строке: наивную и на основе алгоритма Рабина-Карпа. Напишите тесты для них. Сравните производительность.
