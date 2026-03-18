cat("\014")

data_file <- "C:/Users/Georgia/Desktop/farmtech-solutions/data/crop_data.csv"

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

print_metric_block <- function(label, values, unit = "") {
  values <- suppressWarnings(as.numeric(values))
  values <- values[!is.na(values)]

  if (length(values) == 0) {
    cat(label, ": sem dados válidos\n", sep = "")
    return(invisible(NULL))
  }

  suffix <- if (unit == "") "" else paste0(" ", unit)
  cat(sprintf("  Média:           %.2f%s\n", mean(values), suffix))
  cat(sprintf("  Desvio Padrão:   %.2f%s\n", sd(values), suffix))
  cat(sprintf("  Mediana:         %.2f%s\n", median(values), suffix))
  cat(sprintf("  Mínimo:          %.2f%s\n", min(values), suffix))
  cat(sprintf("  Máximo:          %.2f%s\n", max(values), suffix))
  cat(sprintf("  Variância:       %.2f\n", var(values)))
}

main <- function() {
  print_header("FarmTech Solutions - Análise Estatística")

  if (!file.exists(data_file)) {
    cat("ERRO: Arquivo de dados não encontrado!\n")
    cat("Caminho esperado:", data_file, "\n\n")
    cat("Instruções:\n")
    cat("1. Verifique se o arquivo crop_data.csv está na pasta correta\n")
    cat("2. Confirme se o nome do arquivo está exatamente como 'crop_data.csv'\n")
    cat("3. Execute este script novamente\n\n")
    return()
  }

  cat("📂 Carregando dados de:", data_file, "\n")
  crop_data <- read.csv(data_file, header = TRUE, stringsAsFactors = FALSE)

  if (nrow(crop_data) == 0) {
    cat("\nO arquivo está vazio. Adicione dados e tente novamente.\n\n")
    return()
  }

  numeric_columns <- c("area_m2", "rows", "row_length_m", "input_amount_ml_per_m", "total_input_liters")
  for (col in numeric_columns) {
    if (col %in% names(crop_data)) {
      crop_data[[col]] <- suppressWarnings(as.numeric(crop_data[[col]]))
    }
  }

  cat("✓ Dados carregados com sucesso!\n")
  cat("✓ Total de registros:", nrow(crop_data), "\n\n")

  print_divider()
  cat("RESUMO DOS DADOS\n")
  print_divider()
  print(crop_data)
  cat("\n")

  print_header("Estatísticas - Área de Plantio (m²)")
  print_metric_block("Área", crop_data$area_m2, "m²")

  print_header("Estatísticas - Número de Ruas")
  print_metric_block("Ruas", crop_data$rows, "ruas")

  print_header("Estatísticas - Comprimento das Ruas (m)")
  print_metric_block("Comprimento", crop_data$row_length_m, "m")

  print_header("Estatísticas - Quantidade de Insumo (mL/m)")
  print_metric_block("Quantidade por metro", crop_data$input_amount_ml_per_m, "mL/m")

  print_header("Estatísticas - Total de Insumo (litros)")
  print_metric_block("Total de insumo", crop_data$total_input_liters, "L")

  print_header("Estatísticas por Tipo de Cultura")
  crop_types <- unique(crop_data$crop_type)

  for (crop in crop_types) {
    crop_subset <- subset(crop_data, crop_type == crop)
    cat("\n", crop, "\n", sep = "")
    print_divider()
    cat(sprintf("  Quantidade de registros: %d\n", nrow(crop_subset)))
    cat(sprintf("  Área média:              %.2f m²\n", mean(crop_subset$area_m2, na.rm = TRUE)))
    cat(sprintf("  Desvio padrão (área):    %.2f m²\n", sd(crop_subset$area_m2, na.rm = TRUE)))
    cat(sprintf("  Média de ruas:           %.2f\n", mean(crop_subset$rows, na.rm = TRUE)))
    cat(sprintf("  Comprimento médio:       %.2f m\n", mean(crop_subset$row_length_m, na.rm = TRUE)))
    cat(sprintf("  Insumo médio:            %.2f mL/m\n", mean(crop_subset$input_amount_ml_per_m, na.rm = TRUE)))
    cat(sprintf("  Total médio de insumo:   %.2f L\n", mean(crop_subset$total_input_liters, na.rm = TRUE)))
    cat("\n")
  }

  print_header("Insights Adicionais")
  total_area <- sum(crop_data$area_m2, na.rm = TRUE)
  total_input <- sum(crop_data$total_input_liters, na.rm = TRUE)
  cat(sprintf("  Área total cultivada:         %.2f m² (%.2f hectares)\n", total_area, total_area / 10000))
  cat(sprintf("  Total de insumos estimado:    %.2f L\n", total_input))

  avg_area_by_crop <- aggregate(area_m2 ~ crop_type, data = crop_data, FUN = mean)
  largest_crop <- avg_area_by_crop[which.max(avg_area_by_crop$area_m2), ]
  cat(sprintf("  Cultura com maior área média: %s (%.2f m²)\n", largest_crop$crop_type, largest_crop$area_m2))

  cat("\n")
  print_divider()
  cat("Análise concluída com sucesso!\n")
  print_divider()
  cat("\n")
}

tryCatch({
  main()
}, error = function(e) {
  cat("\nERRO durante a análise:\n")
  cat(conditionMessage(e), "\n\n")
})