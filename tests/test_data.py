html_raw_and_expected_a_href = [
    (
        """
<div class="main-navbar__section main-navbar__section_right">
  <a href="https://habrahabr.ru/auth/login/" id="login" class="btn btn_x-large btn_navbar_login">Войти</a>
  <a href="https://habrahabr.ru/auth/register/" class="btn btn_x-large btn_navbar_registration">Регистрация</a>
</div>
""",
        f"""
<div class="main-navbar__section main-navbar__section_right">
  <a class="btn btn_x-large btn_navbar_login" href="/auth/login/" id="login">Войти</a>
  <a class="btn btn_x-large btn_navbar_registration" href="/auth/register/">Регистрация</a>
</div>
"""
    ),
    (
        """
<div class="dropdown-container dropdown-container_flows">
    <ul class="n-dropdown-menu n-dropdown-menu_flows">
        <li class="n-dropdown-menu__item">
          <a href="https://habrahabr.ru/flows/develop/" class="n-dropdown-menu__item-link n-dropdown-menu__item-link_flow">Разработка</a>
        </li>
        <li class="n-dropdown-menu__item">
          <a href="https://habrahabr.ru/flows/admin/" class="n-dropdown-menu__item-link n-dropdown-menu__item-link_flow">Администрирование</a>
        </li>
        <li class="n-dropdown-menu__item">
          <a href="https://habrahabr.ru/flows/design/" class="n-dropdown-menu__item-link n-dropdown-menu__item-link_flow">Дизайн</a>
        </li>
        <li class="n-dropdown-menu__item">
          <a href="https://habrahabr.ru/flows/management/" class="n-dropdown-menu__item-link n-dropdown-menu__item-link_flow">Управление</a>
        </li>
        <li class="n-dropdown-menu__item">
          <a href="https://habrahabr.ru/flows/marketing/" class="n-dropdown-menu__item-link n-dropdown-menu__item-link_flow">Маркетинг</a>
        </li>
        <li class="n-dropdown-menu__item">
          <a href="https://habrahabr.ru/flows/misc/" class="n-dropdown-menu__item-link n-dropdown-menu__item-link_flow">Разное</a>
        </li>
    </ul>
</div>
""",
"""
<div class="dropdown-container dropdown-container_flows">
    <ul class="n-dropdown-menu n-dropdown-menu_flows">
        <li class="n-dropdown-menu__item">
          <a href="/flows/develop/" class="n-dropdown-menu__item-link n-dropdown-menu__item-link_flow">Разработка</a>
        </li>
        <li class="n-dropdown-menu__item">
          <a href="/flows/admin/" class="n-dropdown-menu__item-link n-dropdown-menu__item-link_flow">Администрирование</a>
        </li>
        <li class="n-dropdown-menu__item">
          <a href="/flows/design/" class="n-dropdown-menu__item-link n-dropdown-menu__item-link_flow">Дизайн</a>
        </li>
        <li class="n-dropdown-menu__item">
          <a href="/flows/management/" class="n-dropdown-menu__item-link n-dropdown-menu__item-link_flow">Управление</a>
        </li>
        <li class="n-dropdown-menu__item">
          <a href="/flows/marketing/" class="n-dropdown-menu__item-link n-dropdown-menu__item-link_flow">Маркетинг</a>
        </li>
        <li class="n-dropdown-menu__item">
          <a href="/flows/misc/" class="n-dropdown-menu__item-link n-dropdown-menu__item-link_flow">Разное</a>
        </li>
    </ul>
</div>
"""
    ),
    (
"""
<div class="bmenu">
 <a class="current" href="https://habrahabr.ru?utm_source=tm_habrahabr&amp;utm_medium=tm_top_panel&amp;utm_campaign=tm_promo">Хабрахабр</a>
</div>
""",
"""
<div class="bmenu">
 <a class="current" href="/?utm_source=tm_habrahabr&amp;utm_medium=tm_top_panel&amp;utm_campaign=tm_promo">Хабрахабр</a>
</div>
"""
    ),
    (
"""
<a>A tag without href</a>
""",
"""
<a>A tag without href</a>
"""
    )
]

html_raw_and_expected_text = [
    (
        """
<p>Inside p tag</p>
""",
        """
<p>1</p>
"""
    ),
    (
        """
<div>Inside div tag</div>
""",
        """
<div>1</div>
"""
    ),
    (
        """
<h1>H1 is here!</h1>
""",
        """
<h1>1</h1>
"""
    ),
    (
        """
<h2>This is H2!</h2>
""",
        """
<h2>1</h2>
"""
    ),
    (
        """
<h3>Wow! h3!</h3>
""",
        """
<h3>1</h3>
"""
    ),
    (
        """
<h4>AMAZING!</h4>
""",
        """
<h4>1</h4>
"""
    ),
    (
        """
<a href="http://example.com/a-tag/">a tag</a>
""",
        """
<a href="http://example.com/a-tag/">1</a>
"""
    ),
    (
        """
<custom>Is it possible?</custom>
""",
        """
<custom>1</custom>
"""
    ),
    (
        """
<script>someScript.js</script>
""",
        """
<script>someScript.js</script>
"""
    ),
    (
        """
<ul>
 <li>One text</li>
 <li>Another text</li>
</ul>
""",
        """
<ul>
 <li>1</li>
 <li>1</li>
</ul>
"""
    ),
    (
        """
<div>Nested <strong>formatted</strong> string</div>
""",
        """
<div>1<strong>1</strong>1</div>
"""
    ),
    (
        """
<div> Nested <i>italic</i> text</div>
""",
        """
<div>1<i>1</i>1</div>
"""
    ),
    (
"""
<form action="/search/#h" method="get" class="search-form" id="search-form">
  <!-- Я вернулся братиш, после стольких лет разлуки:) -->
</form>
""",
"""
<form action="/search/#h" method="get" class="search-form" id="search-form">
  <!-- Я вернулся братиш, после стольких лет разлуки:) -->
</form>
"""
    ),
    (
"""
<!DOCTYPE html>
<html></html>
""",
"""
<!DOCTYPE html>
<html></html>
"""
    )
]

html_raw_and_expected_links = [
    (
        """
<link rel="apple-touch-icon-precomposed" sizes="152x152" href="/images/favicons/apple-touch-icon-152x152.png" />
""",
        """
<link rel="apple-touch-icon-precomposed" sizes="152x152" href="https://habrahabr.ru/images/favicons/apple-touch-icon-152x152.png" />
"""
    ),
    (
        """
<link title="Хабрахабр / Лучшие публикации за сутки" type="application/rss+xml" rel="alternate" href="https://habrahabr.ru/rss/best/"/>
""",
        """
<link title="Хабрахабр / Лучшие публикации за сутки" type="application/rss+xml" rel="alternate" href="https://habrahabr.ru/rss/best/"/>
"""
    ),
]
