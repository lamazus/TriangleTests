<h2>Triangle Tests</h2>
<div>Репозиторий создан для демонстрации навыков написания автотестов на языке Python. Объектом для тестирования выступила форма, являющаяся тренажёром для тестировщика (https://playground.learnqa.ru/puzzle/triangle)</div>  
<h3>Инструменты</h3>
<ul>
  <li>Python</li>
  <li>PyTest</li>
  <li>Selenium</li>
  <li>ChromeDriver/GeckoDriver</li>
</ul>
<h3>Установка и запуск</h3>
<p>Все команды необходимо вводить в терминале, находясь в корневой директории проекта</p>
<ol>
  <li>Создать виртуальное окружение:
  <pre>python -m venv .</pre></li>
  <li>Активировать виртуальное окружение:
  <pre>.\Scripts\activate</pre></li>
  <li>Установить зависимости из файла requirements.txt:
  <pre>pip install -r requirements.txt</pre></li>
  <li>Запустить тест. <i>Браузер для тестирования можно указать явно с применением флага --browser=*value*. Поддерживается Chrome(по умолчанию) и Firefox.</i>):
  <pre>pytest --browser=Chrome --tb=line .\tests\test_triangle_page.py</pre></li>
  </li>
</ol>
