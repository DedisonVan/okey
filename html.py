from bs4 import BeautifulSoup

html = """<html lang="uk-UA" style="height:100%;"><head><style type="text/css">@charset "UTF-8";[ng\:cloak],[ng-cloak],[data-ng-cloak],[x-ng-cloak],.ng-cloak,.x-ng-cloak,.ng-hide:not(.ng-hide-animate){display:none !important;}ng\:form{display:block;}.ng-animate-shim{visibility:hidden;}.ng-anchor{position:absolute;}</style>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<meta name="apple-mobile-web-app-title" content="На Урок!">
<meta name="msapplication-TileColor" content="#5362c2">
<link rel="icon" href="/favicon.ico" type="image/x-icon">
<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
<link rel="manifest" href="//naurok.com.ua/manifest_push.json">
<meta name="csrf-param" content="_csrf">
<meta name="csrf-token" content="PQg7FqbXkPhguMkOXdnxiV2Wmla_LfGrtdB9ScGRVB97e2h_xaWnwSyJvWQ_vr7sGfreI5JenMrm5x8Ym8Rscw==">
<title>Результати: Е.А.По "Золотий жук", 7 клас</title>
<meta name="google-site-verification" content="_PAYSIZqXxorQuFLK8-yW4jkm-0L1wmWwzeF7nncqtU">
<meta name="robots" content="NOINDEX, NOFOLLOW">
<meta property="fb:app_id" content="589149888143238">
<meta property="og:locale" content="uk_UA">
<link href="/assets/f0db75bd7fb3b61fd5c2b967f1a77e3e/css/bootstrap.css" rel="stylesheet">
<link href="/js/vendor/bower/angular-confirm/dist/angular-confirm.min.css" rel="stylesheet">
<link href="/js/vendor/bower/angular-ui-notification/dist/angular-ui-notification.min.css" rel="stylesheet">
<link href="/css/quill.snow.css" rel="stylesheet">
<link href="/css/quill.bubble.css" rel="stylesheet">
<link href="/css/site.full.css?v1.37.11" rel="stylesheet"> 
<script type="text/javascript" async="" src="https://www.googletagmanager.com/gtag/js?id=G-1R05Q72V2L&amp;l=dataLayer&amp;cx=c" nonce="NBEUuxqg"></script><script type="text/javascript" async="" src="https://www.google-analytics.com/analytics.js" nonce="NBEUuxqg"></script><script type="text/javascript" async="" src="https://www.google-analytics.com/analytics.js" nonce="NBEUuxqg"></script><script async="" src="https://www.googletagmanager.com/gtm.js?id=GTM-KV2LQMH"></script><script src="https://connect.facebook.net/signals/config/186487121900322?v=2.9.96&amp;r=stable" async=""></script><script src="https://connect.facebook.net/signals/config/2848658688748262?v=2.9.96&amp;r=stable" async=""></script><script async="" src="https://connect.facebook.net/en_US/fbevents.js"></script><script async="" src="https://www.googletagmanager.com/gtag/js?id=UA-108352460-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-108352460-1');
</script>

<script nonce="NBEUuxqg">
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
document,'script','https://connect.facebook.net/en_US/fbevents.js');

fbq('init', '2848658688748262');
fbq('set','agent','tmgoogletagmanager', '2848658688748262');
fbq('track', "PageView");
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=2848658688748262&ev=PageView&noscript=1"
/></noscript>

<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-KV2LQMH');</script>

<script>
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({
        'event' : 'userId_search',
        'userId' : '1028935'
      })
      </script>

<script>
      !function(f,b,e,v,n,t,s)
      {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
      n.callMethod.apply(n,arguments):n.queue.push(arguments)};
      if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
      n.queue=[];t=b.createElement(e);t.async=!0;
      t.src=v;s=b.getElementsByTagName(e)[0];
      s.parentNode.insertBefore(t,s)}(window, document,'script',
      'https://connect.facebook.net/en_US/fbevents.js');
      fbq('init', '186487121900322');
      fbq('track', 'PageView');
    </script>
<noscript><img height="1" width="1" style="display:none"
      src="https://www.facebook.com/tr?id=186487121900322&ev=PageView&noscript=1"
    /></noscript>

<script src="https://apis.google.com/js/platform.js" async="" defer="" gapi_processed="true"></script>
<style>.cke{visibility:hidden;}</style></head>
<body style="margin:0; min-height:100%; height:100%; display:block; position: relative; line-height: 22px;">

<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KV2LQMH"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>

<nav id="w0" class="navbar-inverse navbar-static-top main-nav navbar" style="background: #40596b; padding:10px; min-height:auto; box-shadow:none;">
<div class="container">
<div class="row">
<div class="col-md-4 col-sm-4 col-xs-4">
</div>
<div class="col-md-4 col-sm-4 col-xs-4">
<div class="text-center">
<img src="/img/logo.png" height="40" alt="На Урок для вчителя">
</div>
</div>
<div class="col-md-4 col-sm-4 col-xs-4">
</div>
</div>
</div>
</nav>
<div class="homework-result-page">
<div class="container">
<div class="row">
<div class="col-md-12">
<div class="homework-result-info animated fadeIn">
<div class="homework-result-head">
<div class="row">
<div class="col-md-9 col-sm-8 col-xs-7">
<div class="homework-personal-stat-test">Е.А.По "Золотий жук", 7 клас</div>
<div style="font-size:14px; line-height:1.5;">
<div>ДЗ: Е.А.По "Золотий жук", 7 клас</div>
<div>Вчитель: Валерий Ковельков </div>
<div>Виконав(ла): Олег Тинькоф</div>
<div>17/02/2023 о 11:33</div>
</div>
</div>
<div class="col-md-3 col-sm-4 col-xs-5">
<div class="homework-personal-stat-number">24 <span>запитань</span></div>
</div>
</div>
</div>
<div class="row homework-personal-stat-row">
<div class="col-md-9 col-sm-8 col-xs-7">
<div class="homework-personal-stat-label text-right">Оцінка</div>
</div>
<div class="col-md-3 col-sm-4 col-xs-5">
<div class="homework-personal-stat-value"><span>0 / 12</span> балів</div>
</div>
</div>
<div class="row homework-personal-stat-row">
<div class="col-md-3 col-sm-3 col-xs-12">
<div class="homework-personal-stat-label">Сума балів</div>
</div>
<div class="col-md-3 col-sm-3 col-xs-12">
<div class="homework-personal-stat-value"><span>0 / 12</span></div>
</div>
<div class="col-md-3 col-sm-3 col-xs-12">
<div class="homework-personal-stat-label text-right">Результат</div>
</div>
<div class="col-md-3 col-sm-3 col-xs-12">
<div class="homework-personal-stat-value"><span>0</span> %</div>
</div>
</div>
<div class="row homework-personal-stat-row">
<div class="col-md-3  col-sm-3">
<div class="homework-personal-stat-label">Точність</div>
</div>
<div class="col-md-9 col-sm-9">
<div class="progress">
<div class="progress-bar" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%;">
0%
</div>
<div class="correct-label">Правильно</div>
<div class="incorrect-label">Неправильно</div>
</div>
</div>
</div>
<div class="row homework-personal-stat-row">
<div class="col-md-4  col-sm-4 col-xs-6">
<div class="homework-personal-stat-value"><span>0</span> правильних</div>
</div>
<div class="col-md-4  col-sm-4 col-xs-6">
<div class="homework-personal-stat-value"><span>1</span> неправильних</div>
</div>
<div class="col-md-4  col-sm-4 hidden-xs">
<div class="homework-personal-stat-value"><span>23</span> пропущено</div>
</div>
</div>
<div class="row homework-personal-stat-row">
<div class="col-md-6  col-sm-6  col-xs-6">
<div class="homework-personal-stat-value">Всього часу <span>10 сек</span></div>
</div>
<div class="col-md-6  col-sm-6  col-xs-6">
<div class="homework-personal-stat-value">Ср. час / запитання <span>10 сек</span></div>
</div>
</div>
</div>
<div class="homework-review-title">Результати інших учасників</div>
<div class="homework-rating animated tada" style="margin-top:10px;">
<div class="homework-student-result">
<div class="row">
<div class="col-md-9 col-sm-10 col-xs-10">
<div class="homework-student-name">Олег Тинькоф</div>
<div class="homework-student-point"><span>0</span> бал</div>
</div>
<div class="col-md-3 col-sm-2 col-xs-2">
<div class="homework-student-result-place result-place1 animated bounceIn">1<span>місце</span></div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="container">
<div class="dashboard-sidebar" style="margin-top:20px;">
<div class="row">
<div class="col-md-6 col-sm-6  col-xs-12">
<div class="instagram-follow">
<a target="_blank" href="https://www.instagram.com/naurok.ua/">
<div class="row">
<div class="col-md-3 col-sm-3 col-xs-3">
<img class="animated pulse" src="/img/instagram-icon.png" width="100%">
</div>
<div class="col-md-9 col-sm-8 col-xs-8">
<div style="margin-top:15px;">Слідкуй за «На Урок»<br> в Instagram</div>
</div>
</div>
</a>
</div>
</div>
<div class="col-md-6  col-sm-6  col-xs-12">
<div class="youtube-follow">
<a target="_blank" href="https://www.youtube.com/channel/UCvPcQtWGRlChbwbdYwYueJQ?sub_confirmation=1">
<div class="row">
<div class="col-md-3 col-sm-3 col-xs-3">
<img class="animated pulse" src="/img/youtube-icon.png" width="100%">
</div>
<div class="col-md-9 col-sm-8 col-xs-8">
<div style="margin-top:15px;">Слідкуй за «На Урок»<br> на YouTube</div>
</div>
</div>
</a>
</div>
</div>
</div>
</div>
</div>
<div class="container">
<div class="row">
<div class="col-md-12">
<div class="student-promo-banner" style="margin-top:20px;">
<div class="row">
<div class="col-md-3">
<div class="student-promo-image" style="margin-bottom:0;"><img src="/img/stud/lp/zno.svg" width="100%"></div>
</div>
<div class="col-md-9">
<div class="student-promo-message">Хочеш більше цікавих завдань та корисних знань?</div>
<div class="student-promo-cta text-left">
<a href="https://naurok.ua/course/catalog?grade=7-klas&amp;source=test_results" target="_blank" class="btn btn-default">Авжеж!</a>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="container animated fadeIn">
<div class="homework-result-page">
<div class="homework-review-title">Ознайомитися з відповідями</div>
<div class="library library-single library-test">
<div class="homework-stats">
<div class="content-block failed">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-question-line ">
1. <p><strong>1. Засновником якого жанру літератури вважають Едгара По?</strong></p> <div class="homework-stat-options">
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">1</span> <p>Історичної</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct quiz">2</span> <p>Детективної</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">3</span> <p>Науково-фаниастичої</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">4</span> <p>Античної</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">5</span> <p>Пригодницької</p> <em>— ваша відповідь</em> </div>
</div>
</div>
</div>
</div>
<div class="question-label">0 балів</div>
</div>
</div>
</div>
</div>
<div class="content-block skipped">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-question-line ">
2. <p><strong>2 "Золотий жук" за жанром - це</strong></p> <div class="homework-stat-options">
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">1</span> <p>Роман</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
 <div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct quiz">2</span> <p>Новела</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">3</span> <p>Оповідання</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">4</span> <p>Повість </p> </div>
</div>
</div>
</div>
</div>
<div class="question-label">0 балів</div>
</div>
</div>
</div>
</div>
<div class="content-block skipped">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-question-line ">
3. <p><strong>3. Композиція твору </strong></p> <div class="homework-stat-options">
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">1</span> <p>Кільцева,(повторюється початок і кінець)</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct quiz">2</span> <p>Оповідання у оповіданні</p>  </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">3</span> <p>Розповідь від імені героя </p> </div>
</div>
</div>
</div>
</div>
<div class="question-label">0 балів</div>
</div>
</div>
</div>
</div>
<div class="content-block skipped">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-question-line ">
4. <p><strong>4.Назвати героїв твору</strong></p><p><strong> " Золотий жук"</strong></p> <div class="homework-stat-options">
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct multiquiz">1</span> <p>Дослідник Вільям Легран</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect multiquiz">2</span> <p>Доктор Ватсон</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct multiquiz">3</span> <p>Слуга Джупітер</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect multiquiz">4</span> <p>Приватний детектив Шерлок Холмс</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct multiquiz">5</span> <p>Оповідач</p> </div>
</div>
</div>
</div>
</div>
<div class="question-label">0 балів</div>
</div>
</div>
</div>
</div>
<div class="content-block skipped">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-question-line ">
5. <p><strong>5.Вільям Легран був нащадком</strong></p> <div class="homework-stat-options">
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">1</span> <p>Ролу лордів</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">2</span> <p>Із роду багатих купців </p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
 <div class="homework-stat-option-value correct">
<span class="correct quiz">3</span> <p>аристократичного роду</p> </div>
</div>
</div>
</div>
</div>
<div class="question-label">0 балів</div>
</div>
</div>
</div>
</div>
<div class="content-block skipped">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-question-line ">
6. <p><strong>6 Куди переїхав Легран, покинувши Новий Орлеан?</strong></p> <div class="homework-stat-options">
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">1</span> <p>На безлюдний острів Робінзона </p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct quiz">2</span> <p>Пустельний острів в Антлантичному океані</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">3</span> <p>Безлюдний острів в Тихому океані</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">4</span> <p>У гори Анди</p> </div>
</div>
</div>
</div>
</div>
<div class="question-label">0 балів</div>
</div>
</div>
</div>
</div>
<div class="content-block skipped">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-question-line ">
7. <p><strong>7.Чим займася Легран на новому місці?</strong></p> <div class="homework-stat-options">
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">1</span> <p>Читав книжки</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">2</span> <p>Збирав рослини для гербарію</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct quiz">3</span> <p>Збирав рідкісних комах</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">4</span> <p>Піднімався на велику скелю і дивися у підзорну трубу</p> </div>
</div>
 </div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">5</span> <p>Прогулянки берегом моря</p> </div>
</div>
</div>
</div>
</div>
<div class="question-label">0 балів</div>
</div>
</div>
</div>
</div>
<div class="content-block skipped">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-question-line ">
8. <p><strong>8.Джупітер - це</strong></p> <div class="homework-stat-options">
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct quiz">1</span> <p>Старий слуга Леграна</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">2</span> <p>Найкращий друг Леграна</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">3</span> <p>Близький родич Леграна</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
 <div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">4</span> <p>Військовий із острова </p> </div>
</div>
</div>
</div>
</div>
<div class="question-label">0 балів</div>
</div>
</div>
</div>
</div>
<div class="content-block skipped">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-question-line ">
9. <p><strong>9.Що знайшов дивного Легран на березі під час прогулянки?</strong></p> <div class="homework-stat-options">
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">1</span> <p>Золотий череп</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct quiz">2</span> <p>Золотого жука</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">3</span> <p>Золоті монети</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">4</span> <p>Золотий глечик</p> </div>
</div>
</div>
</div>
</div>
<div class="question-label">0 балів</div>
</div>
</div>
</div>
</div>
<div class="content-block skipped">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-question-line ">
10. <p><strong>10.На що були схожі цяточки на спині знайденого жука ?</strong></p> <div class="homework-stat-options">
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">1</span> <p>Іспанський ніж</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">2</span> <p>Морські русалку</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct quiz">3</span> <p>На череп із кістками навхрест</p> </div>
</div>
</div>
</div>
</div>
<div class="question-label">0 балів</div>
</div>
</div>
</div>
</div>
<div class="content-block skipped">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-question-line ">
11. <p><strong>11.Яке хоббі було у Леграна?</strong></p>  <div class="homework-stat-options">
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">1</span> <p>Мав колекцію марок</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct quiz">2</span> <p>Мав колекцію рідкісних комах</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">3</span> <p>Мав колекцію старовинних монет</p> </div>
</div>
</div>
</div>
</div>
<div class="question-label">0 балів</div>
</div>
</div>
</div>
</div>
<div class="content-block skipped">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-question-line ">
12. <p><strong>12. Що привернуло увагу Леграна, коли він роздивлявся жука? Оберіть декілька варіантів.</strong></p> <div class="homework-stat-options">
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct multiquiz">1</span> <p>Яскраво золота фарба жука</p> </div>
</div>
</div>
</div>
 <div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect multiquiz">2</span> <p>Товсті вусики</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct multiquiz">3</span> <p>Був надто важкий </p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct multiquiz">4</span> <p>Чорні цятки виблискували золотом</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct multiquiz">5</span> <p>Крильця мали металевий блиск</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect multiquiz">6</span> <p>Не було нічого дивного</p> </div>
</div>
</div>
</div>
</div>
<div class="question-label">0 балів</div>
</div>
</div>
</div>
</div>
 <div class="content-block skipped">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-question-line ">
13. <p><strong>13. На чому Легран намалював обриси жука?</strong></p> <div class="homework-stat-options">
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">1</span> <p>На шпалерах</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct quiz">2</span> <p>На клаптику пергамента</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">3</span> <p>У робочому зошиті</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">4</span> <p>У дослідницькому журналі</p> </div>
</div>
</div>
</div>
</div>
<div class="question-label">0 балів</div>
</div>
</div>
</div>
</div>
<div class="content-block skipped">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-question-line ">
14. <p><strong>14. Куди збиралася Легран?</strong></p> <div class="homework-stat-options">
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">1</span> <p>На Північний полюс, щоб побачити полярне сяйво</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct quiz">2</span> <p>В експедицію , яка принесе йому скарби і багатство</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">3</span> <p>Переїхати знову у Новий Орлеан і почати писати нову книгу </p> </div>
</div>
</div>
</div>
</div>
<div class="question-label">0 балів</div>
</div>
</div>
</div>
</div>
<div class="content-block skipped">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-question-line ">
15. <p><strong>15 .Як Леграну вдалося прочитати напис на папірусі?</strong></p> <div class="homework-stat-options">
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">1</span> <p>Розглядав його через лупу.&nbsp;</p> </div>
 </div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">2</span> <p>Протер спиртовим розчином.</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct quiz">3</span> <p>Нагрів його над вогнем, обмив водою і просушив на сковорідці.</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">4</span> <p><em>потримав пергамент над вогнем каміна</em></p> </div>
</div>
</div>
</div>
</div>
<div class="question-label">0 балів</div>
</div>
</div>
</div>
</div>
<div class="content-block skipped">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-question-line ">
16. <p><strong>16. Зашифрований надпис на пергаменті називається</strong></p> <div class="homework-stat-options">
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">1</span> <p>Анаграма</p> </div>
</div>
</div>
</div>
 <div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct quiz">2</span> <p>Криптограма</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">3</span> <p>Каліграма</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">4</span> <p>Телеграма</p> </div>
</div>
</div>
</div>
</div>
<div class="question-label">0 балів</div>
</div>
</div>
</div>
</div>
<div class="content-block skipped">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-question-line ">
17. <p><strong>17.На яке дерево заліз слуга Джупітер?</strong></p> <div class="homework-stat-options">
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct quiz">1</span> <p>Тюльпанове</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
 <span class="incorect quiz">2</span> <p>Бамбукове</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">3</span> <p>Баобабове</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">4</span> <p>Кипарисове</p> </div>
</div>
</div>
</div>
</div>
<div class="question-label">0 балів</div>
</div>
</div>
</div>
</div>
<div class="content-block skipped">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-question-line ">
18. <p><strong>18.Що побачив слуга, коли добрався до сьомої гілки дерева?</strong></p> <div class="homework-stat-options">
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">1</span> <p>Піратську емблему</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">2</span> <p>Такого самого золотого жука</p> </div>
 </div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct quiz">3</span> <p>Череп, прибитий цвяхом</p> </div>
</div>
</div>
</div>
</div>
<div class="question-label">0 балів</div>
</div>
</div>
</div>
</div>
<div class="content-block skipped">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-question-line ">
19. <p><strong>19 .Що треба було зробити, щоб знайти місцевість з кладом?</strong></p> <div class="homework-stat-options">
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct quiz">1</span> <p>Через ліве око черепа пропустити жука і спустити вниз </p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">2</span> <p>Пропустити жука через праве око черепа</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">3</span> <p>Зняти обережно череп </p> </div>
</div>
</div>
</div>
 </div>
<div class="question-label">0 балів</div>
</div>
</div>
</div>
</div>
<div class="content-block skipped">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-question-line ">
20. <p><strong>20. Яку помилку допустив слуга Джупітер , коли не знайшли місце з кладом ?</strong></p> <div class="homework-stat-options">
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct quiz">1</span> <p>Був лівша і пропустив через праве око </p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">2</span> <p>Слуга зовсім не зрозумів, що йому робити</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">3</span> <p>Його привабили золоті монети біля черепа, які він забрав</p> </div>
</div>
</div>
</div>
</div>
<div class="question-label">0 балів</div>
</div>
</div>
</div>
</div>
<div class="content-block skipped">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-question-line ">
21. <p><strong>21.Що друзі знайшли у розкопаному схові?</strong></p> <div class="homework-stat-options">
 <div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">1</span> <p>пусту дерев’яну скриню</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct quiz">2</span> <p>гроші, коштовності, золото;</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">3</span> <p>Скриню із зброєю </p> </div>
</div>
</div>
</div>
</div>
<div class="question-label">0 балів</div>
</div>
</div>
</div>
</div>
<div class="content-block skipped">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-question-line ">
22. <p><strong>22. Що означав череп із кістками навхрест?</strong></p> <div class="homework-stat-options">
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">1</span> <p>Піратський ніж</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">2</span> <p>Піратський прапор </p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct quiz">3</span> <p>Піратську емблему</p> </div>
</div>
</div>
</div>
</div>
<div class="question-label">0 балів</div>
</div>
</div>
</div>
</div>
<div class="content-block skipped">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-question-line ">
23. <p><strong>23. Визначте тему оповідання " Золотий жук" Едгара По</strong></p> <div class="homework-stat-options">
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">1</span> <p>золота лихоманка;</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">2</span> <p>розповідь про неіснуючу комаху;</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct quiz">3</span> <p>пошук скарбів, захованих піратами;</p>  </div>
</div>
</div>
</div>
</div>
<div class="question-label">0 балів</div>
</div>
</div>
</div>
</div>
<div class="content-block skipped">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-question-line ">
24. <p><strong>24 Яка ідея оповідання "Золотий жук"?</strong></p> <div class="homework-stat-options">
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">1</span> <p>захоплива подорож за скарбами</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value correct">
<span class="correct quiz">2</span> <p>Розповідь про таємницю золотого жука.</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">3</span> <p>розгадування таємниці захованого скарбу.</p> </div>
</div>
</div>
</div>
<div class="homework-stat-option-line">
<div class="row">
<div class="col-md-12">
<div class="homework-stat-option-value incorect">
<span class="incorect quiz">4</span> <p>гімн людському інтелекту.</p> </div>
</div>
 </div>
</div>
</div>
<div class="question-label">0 балів</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<script src="https://www.gstatic.com/firebasejs/4.6.0/firebase.js"></script>
<script>
  // Initialize Firebase
  var config = {
    apiKey: "AIzaSyDqZNEmjh0EBu1hQqQR22QswP2ZFoOAnTE",
    authDomain: "naurok-com-ua.firebaseapp.com",
    databaseURL: "https://naurok-com-ua.firebaseio.com",
    projectId: "naurok-com-ua",
    storageBucket: "naurok-com-ua.appspot.com",
    messagingSenderId: "756484883010"
  };
  firebase.initializeApp(config);
</script>
<script type="application/ld+json">
{
  "@context": "http://schema.org",
  "@type": "Organization",
  "name": "«На Урок»",
  "url": "https://naurok.com.ua",
  "logo": "https://naurok.com.ua/img/logo_new3.png",
  "sameAs": [
    "https://www.facebook.com/naurok.com.ua",
    "https://www.facebook.com/groups/naurok.com.ua/",
    "https://plus.google.com/116882310924056429434",
    "https://www.youtube.com/channel/UCMCYaKTwZ1Olw1fuzLvgA_Q"
  ]
}
</script>
<script src="/assets/cb30fc59caa0617bdb70be372b05a914/jquery.js"></script>
<script src="/assets/af03f6b16f606305d9cf827034cc8968/yii.js"></script>
<script src="/js/app_core.js?4.1"></script>
<script src="/js/lib/ckeditor/ckeditor.js"></script>
<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.7.8/angular-sanitize.min.js"></script>
<script src="/js/vendor/bower/angular-confirm/dist/angular-confirm.min.js"></script>
<script src="/js/vendor/bower/angular-ui-notification/dist/angular-ui-notification.min.js"></script>
<script src="/js/vendor/bower/angular-ckeditor/angular-ckeditor.min.js"></script>
<script src="/js/quill.min.js"></script>
<script src="/js/ng-quill.js"></script>
<script src="/js/lib/file/ng-file-upload-shim.min.js"></script>
<script src="/js/lib/file/ng-file-upload.min.js"></script>
<script src="/js/lib/hotkey.js"></script>
<script src="/js/lib/interact.min.js"></script>
<script src="/js/lib/ng-websocket2.js?2"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/2.3.0/socket.io.js"></script>
<script src="/js/lib/socket.min.js?2"></script>
<script src="/js/lib/howler.min.js"></script>
<script src="/js/app_test.test.js?14.33"></script>
<script src="/js/script.full.js?v1.2.5"></script>


</div></div><div id="lightboxOverlay" class="lightboxOverlay" style="display: none;"></div><div id="lightbox" class="lightbox" style="display: none;"><div class="lb-outerContainer"><div class="lb-container"><img class="lb-image" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="><div class="lb-nav"><a class="lb-prev" href=""></a><a class="lb-next" href=""></a></div><div class="lb-loader"><a class="lb-cancel"></a></div></div></div><div class="lb-dataContainer"><div class="lb-data"><div class="lb-details"><span class="lb-caption"></span><span class="lb-number"></span></div><div class="lb-closeContainer"><a class="lb-close"></a></div></div></div></div></body></html>
"""
# создаем объект soup