**1. SELECT** для выбора данных:

SELECT CURRENT_TIMESTAMP();  
  
SELECT name, qualification FROM users;

**2. FROM** для указания источника собираемых данных:

SELECT * FROM users;

**3. WHERE** для выполнения условия:

SELECT * FROM users WHERE id = 10;

**4. AS** для назначения псевдонима таблице или полям:

SELECT first_name AS name FROM users;

**5. JOIN** для объединения строк двух и более таблиц:

SELECT users.name, scores.percentage FROM users   
JOIN scores ON users.id = scores.user_id;

**6. AND, OR** для объединения условий запроса.

_AND_ для проверки всех условий, которые должны быть истинными:

SELECT * FROM users WHERE id = 10 AND qualification = "B.E.";

_OR_ для проверки истинности по крайней мере одного условия:

SELECT * FROM users WHERE gender="male" OR qualification = "B.E.";

**7. LIMIT, OFFSET** для контроля и пропуска числа записей.

_LIMIT_ для контроля числа возвращаемых записей:

SELECT * FROM users LIMIT 10;

_OFFSET_ для пропуска числа записей:

SELECT * FROM users LIMIT 10 OFFSET 5;

Этим запросом возвращается десять записей после пропуска пяти.

_OFFSET без LIMIT не применяется._

**8. IN**  —  это сокращенный метод с несколькими условиями _OR_ для выбора записей по совпадающим значениям:

SELECT * FROM users WHERE qualification IN("B.E.", "M.E.", "M.C.A.");

Этим запросом возвращаются все пользователи с одной из перечисленных в `_In()_` квалификаций.

**9. CASE** для проверки выполнения конкретных условий, с применением простого `_if-else_`:

SELECT id, name,  
CASE   
  WHEN qualification = "B.E." THEN "Bechelors"  
  WHEN qualification = "M.E." THEN "Masters"  
  ELSE graduate   
END AS degree  
FROM users;

Выполнение команды завершается, когда найдено соответствие условию. Возвращается значение, указанное в _THEN_.

Если соответствие не найдено, возвращается значение из _ELSE_. Если в _ELSE_ ничего не указано, возвращается _NULL_.

**10. IS NULL, IS NOT NULL** для проверки значения _null_ и _не null_ соответственно:

SELECT * FROM users WHERE qualification IS NULL;  
  
SELECT * FROM users WHERE qualification IS NOT NULL;

**11. LIKE**  —  это оператор сопоставления с шаблоном, аналог _WHERE_.

Знак процента _(%)_ используется для выявления частичного совпадения:

SELECT * FROM users WHERE name LIKE "al%";

Этим запросом выбираются все записи, в которых имя пользователя начинается с `al`: _Alex_, _Alis_.

А еще так находятся записи с конкретной буквой в заданной позиции в строке:

SELECT * FROM users WHERE name LIKE "_a%";

Этим запросом выполняется поиск записей со второй буквой `a` в имени: _Jane_, _Jack_.

Знаками процента (%) и подчеркивания (_) запрос **LIKE** подстраивается под требования.

_LIKE_ применяется и с оператором логического отрицания _NOT_: _NOT LIKE_.

**12. DISTINCT** для удаления из таблицы повторяющихся записей и получения только уникальных:

SELECT DISTINCT name FROM users;

Этим запросом из результата удаляются пользователи с повторяющимися именами.

**13. EXPLAIN** для получения информации о выполнении запроса в таблице:

EXPLAIN SELECT * FROM users;

Применяется в основном для оптимизации базы данных.

**14. ALTER TABLE** для обновления имеющейся таблицы или столбцов:

ALTER TABLE Customers ADD email varchar(255);

**15. CREATE** для создания таблицы:

CREATE TABLE scores (  
    id int,  
    first_name varchar(255),  
    last_name varchar(255)  
);

**16. DELETE** для удаления записей из таблицы:

DELETE FROM users WHERE id = 10;

**17. UPDATE** для обновления записей таблицы:

UPDATE users SET name = "Joe" WHERE id = 10;

**18. INSERT** для вставки записей в таблицу:

INSERT INTO users(id, first_name, last_name) VALUES(1, "joe", "shoen");  
  
OR  
  
INSERT INTO users VALUES(1, "joe", "shoen");

**19. TRUNCATE** для очистки таблицы:

TRUNCATE TABLE users;

**20. DROP** для удаления таблицы:

DROP TABLE users;

---

### Операторы

**1. GROUP BY** для группировки записей по заданным значениям столбцов:

SELECT COUNT(*) as qualifications FROM users GROUP BY qualification;

Этим запросом возвращается общее число квалификаций с записями, сгруппированными по значениям столбца квалификаций.

**2. ORDER BY** для упорядочения данных указанных столбцов по возрастанию или убыванию:

SELECT * FROM users ORDER BY id ASC;  
  
SELECT * FROM users ORDER BY id, score DESC;

**3. HAVING** используется с _GROUP BY_, так как _WHERE_ не применяется с агрегированными результатами:

SELECT COUNT(id), qualification   
FROM users   
GROUP BY qualification  
HAVING COUNT(id) > 3;

Этим запросом возвращается количество пользователей, сгруппированных по квалификации, где это количество _> 3_.  
 **4. UNION** для объединения результатов двух и более операторов `SELECT`:

SELECT name, email FROM users  
UNION  
SELECT name, email FROM admins;

**5. EXISTS** для проверки наличия любой записи выполняется подзапрос, в зависимости от результата которого возвращается _true_ или _false_:

SELECT EXISTS   
(SELECT name FROM users   
WHERE id = 1) AS isExist;

---

### Функции

**1. COUNT()** для возвращения числа выражения, с условиями или без них:

SELECT COUNT(*) as total_users FROM users;

**2. SUM()** для возвращения общего значения по заданному набору значений:

SELECT SUM(scores) FROM users;

**3. AVG()** для получения среднего значения по заданному набору значений:

SELECT AVG(scores) FROM users;

**4. MIN()** для нахождения минимального значения по заданному набору значений:

SELECT MIN(scores) FROM users;

**5. MAX()** для нахождения максимального значения по заданному набору значений:

SELECT MAX(scores) FROM users;

---