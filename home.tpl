<!-- Tato část kódu je hlavička -->
<!DOCTYPE html>
<html>

<head>
    <title>{{title}}</title>
</head>

<body>
<!-- konec hlavičky -->

<!-- Hlavní tělo stránky -->
    <div>
        <h1>{{title}}</h1>
        <ol>
            % for player in players:
            <li>{{player}}</li>
            % end
        </ol>
    </div>
<!-- konec hlavního těla stránky -->

<!-- Začátek patičky -->
    <footer>
        <p>(c) 2020 by makeITtoday</p>
    </footer>
</body>

</html>
<!-- konec patičky -->
