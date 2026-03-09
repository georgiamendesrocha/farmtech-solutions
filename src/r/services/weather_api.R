required_packages <- c("jsonlite", "httr")

check_and_install <- function(packages) {
  for (pkg in packages) {
    if (!require(pkg, character.only = TRUE, quietly = TRUE)) {
      cat("📦 Instalando pacote:", pkg, "\n")
      install.packages(pkg, repos = "https://cloud.r-project.org/", quiet = TRUE)
      library(pkg, character.only = TRUE)
    }
  }
}

print_header <- function(title) {
  cat("\n")
  cat(rep("=", 70), sep = "")
  cat("\n")
  cat("  ", title, "\n")
  cat(rep("=", 70), sep = "")
  cat("\n\n")
}

print_divider <- function() {
  cat(rep("-", 70), sep = "")
  cat("\n")
}

get_weather_data <- function(latitude, longitude, city_name = "Local selecionado") {
  
  base_url <- "https://api.open-meteo.com/v1/forecast"
  
  params <- list(
    latitude = latitude,
    longitude = longitude,
    current = "temperature_2m,relative_humidity_2m,precipitation,rain,wind_speed_10m,weather_code",
    daily = "temperature_2m_max,temperature_2m_min,precipitation_sum,rain_sum,wind_speed_10m_max",
    timezone = "auto"
  )
  
  cat("Conectando à API Open-Meteo...\n")
  cat("Coordenadas:", latitude, ",", longitude, "\n")
  
  response <- tryCatch({
    GET(base_url, query = params, timeout(10))
  }, error = function(e) {
    cat("Erro ao conectar com a API:", conditionMessage(e), "\n")
    return(NULL)
  })
  
  if (is.null(response)) {
    return(NULL)
  }
  
  if (status_code(response) != 200) {
    cat("Erro na requisição. Código:", status_code(response), "\n")
    return(NULL)
  }
  
  cat("✓ Dados recebidos com sucesso!\n\n")
  
  data <- fromJSON(content(response, "text", encoding = "UTF-8"))
  
  print_header(paste("Clima Atual -", city_name))
  
  current <- data$current
  
  cat(sprintf("  🌡️  Temperatura:        %.1f°C\n", current$temperature_2m))
  cat(sprintf("  💧 Umidade:            %d%%\n", current$relative_humidity_2m))
  cat(sprintf("  🌧️  Precipitação:       %.1f mm\n", current$precipitation))
  cat(sprintf("  💨 Velocidade do Vento: %.1f km/h\n", current$wind_speed_10m))
  cat(sprintf("  📅 Horário:            %s\n", current$time))
  
  weather_desc <- get_weather_description(current$weather_code)
  cat(sprintf("  ☁️  Condição:           %s\n", weather_desc))
  
  print_header("Previsão para os Próximos 7 Dias")
  
  daily <- data$daily
  
  for (i in 1:min(7, length(daily$time))) {
    date <- daily$time[i]
    temp_max <- daily$temperature_2m_max[i]
    temp_min <- daily$temperature_2m_min[i]
    precip <- daily$precipitation_sum[i]
    rain <- daily$rain_sum[i]
    wind_max <- daily$wind_speed_10m_max[i]
    
    cat(sprintf("\n  %s\n", date))
    cat(sprintf("     Temp: %.1f°C - %.1f°C | Chuva: %.1f mm | Vento: %.1f km/h\n",
                temp_min, temp_max, rain, wind_max))
  }
  
  print_header("Insights para Agricultura")
  
  avg_temp <- mean(c(daily$temperature_2m_max, daily$temperature_2m_min), na.rm = TRUE)
  total_rain <- sum(daily$rain_sum, na.rm = TRUE)
  max_wind <- max(daily$wind_speed_10m_max, na.rm = TRUE)
  
  cat(sprintf("  Temperatura média da semana:  %.1f°C\n", avg_temp))
  cat(sprintf("  Total de chuva prevista:      %.1f mm\n", total_rain))
  cat(sprintf("  Vento máximo esperado:        %.1f km/h\n\n", max_wind))
  
  cat("Recomendações:\n\n")
  
  if (total_rain > 50) {
    cat("     • Alto volume de chuva previsto - considere adiar pulverizações\n")
  } else if (total_rain < 10) {
    cat("     • Pouca chuva prevista - planeje irrigação adequada\n")
  } else {
    cat("     • Volume de chuva moderado - condições favoráveis para cultivo\n")
  }
  
  if (avg_temp > 30) {
    cat("     • Temperaturas elevadas - monitore estresse hídrico das plantas\n")
  } else if (avg_temp < 15) {
    cat("     • Temperaturas baixas - atenção com culturas sensíveis ao frio\n")
  } else {
    cat("     • Temperaturas adequadas para maioria das culturas\n")
  }
  
  if (max_wind > 40) {
    cat("     • Ventos fortes previstos - proteja culturas e estruturas\n")
  }
  
  cat("\n")
  print_divider()
}

get_weather_description <- function(code) {
  descriptions <- list(
    "0" = "Céu limpo",
    "1" = "Principalmente limpo",
    "2" = "Parcialmente nublado",
    "3" = "Nublado",
    "45" = "Nevoeiro",
    "48" = "Nevoeiro com geada",
    "51" = "Garoa leve",
    "53" = "Garoa moderada",
    "55" = "Garoa densa",
    "61" = "Chuva leve",
    "63" = "Chuva moderada",
    "65" = "Chuva forte",
    "71" = "Neve leve",
    "73" = "Neve moderada",
    "75" = "Neve forte",
    "80" = "Pancadas de chuva leves",
    "81" = "Pancadas de chuva moderadas",
    "82" = "Pancadas de chuva fortes",
    "95" = "Tempestade",
    "96" = "Tempestade com granizo leve",
    "99" = "Tempestade com granizo forte"
  )
  
  code_str <- as.character(code)
  if (code_str %in% names(descriptions)) {
    return(descriptions[[code_str]])
  } else {
    return(paste("Código", code))
  }
}

main <- function() {
  print_header("FarmTech Solutions - Dados Meteorológicos")
  
  cat("Instalando/carregando pacotes necessários...\n")
  check_and_install(required_packages)
  
  cat("\n✓ Pacotes carregados com sucesso!\n")
  
  print_divider()
  cat("\nEscolha a localização:\n\n")
  cat("1. São Paulo, SP (Região Sudeste)\n")
  cat("2. Cuiabá, MT (Centro-Oeste - Soja)\n")
  cat("3. Patrocínio, MG (Sudeste - Café)\n")
  cat("4. Londrina, PR (Sul - Soja)\n")
  cat("5. Inserir coordenadas manualmente\n\n")
  
  choice <- readline(prompt = "Digite sua escolha (1-5): ")
  
  locations <- list(
    "1" = list(lat = -23.5505, lon = -46.6333, name = "São Paulo, SP"),
    "2" = list(lat = -15.6014, lon = -56.0979, name = "Cuiabá, MT"),
    "3" = list(lat = -18.9436, lon = -46.9958, name = "Patrocínio, MG"),
    "4" = list(lat = -23.3045, lon = -51.1696, name = "Londrina, PR")
  )
  
  if (choice %in% names(locations)) {
    loc <- locations[[choice]]
    get_weather_data(loc$lat, loc$lon, loc$name)
  } else if (choice == "5") {
    cat("\n")
    lat <- as.numeric(readline(prompt = "Digite a latitude: "))
    lon <- as.numeric(readline(prompt = "Digite a longitude: "))
    
    if (!is.na(lat) && !is.na(lon)) {
      get_weather_data(lat, lon)
    } else {
      cat("Coordenadas inválidas!\n")
    }
  } else {
    cat("Opção inválida!\n")
  }
  
  cat("\n")
  print_divider()
  cat("Dados fornecidos por: Open-Meteo API (https://open-meteo.com)\n")
  cat("API gratuita e confiável para dados meteorológicos\n")
  print_divider()
  cat("\n")
}

tryCatch({
  main()
}, error = function(e) {
  cat("\n ERRO durante a execução:\n")
  cat(conditionMessage(e), "\n\n")
  cat("Certifique-se de que você tem conexão com a internet.\n")
})
