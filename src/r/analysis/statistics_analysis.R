cat("\014")

print_header <- function(title) {
  cat("\n")
  cat(rep("=", 60), sep = "")
  cat("\n")
  cat("  ", title, "\n")
  cat(rep("=", 60), sep = "")
  cat("\n\n")
}

print_divider <- function() {
  cat(rep("-", 60), sep = "")
  cat("\n")
}

main <- function() {
  print_header("FarmTech Solutions - Análise Estatística")
  
  data_file <- "../../data/crop_data.csv"
  
  if (!file.exists(data_file)) {
    cat("ERRO: Arquivo de dados não encontrado!\n")
    cat("Caminho esperado:", data_file, "\n\n")
    cat("Instruções:\n")
    cat("1. Execute primeiro a aplicação Python (main.py)\n")
    cat("2. Adicione alguns registros de culturas\n")
    cat("3. Escolha a opção 'Sair' no menu para exportar os dados\n")
    cat("4. Execute este script novamente\n\n")
    return()
  }
  
  cat("📂 Carregando dados de:", data_file, "\n")
  crop_data <- read.csv(data_file, header = TRUE, stringsAsFactors = FALSE)
  
  if (nrow(crop_data) == 0) {
    cat("\n O arquivo está vazio. Adicione dados usando a aplicação Python.\n\n")
    return()
  }
  
  cat("✓ Dados carregados com sucesso!\n")
  cat("✓ Total de registros:", nrow(crop_data), "\n\n")
  
  print_divider()
  cat("RESUMO DOS DADOS\n")
  print_divider()
  print(crop_data)
  cat("\n")
  
  print_header("Estatísticas - Área de Plantio (m²)")
  
  area_mean <- mean(crop_data$area_m2)
  area_sd <- sd(crop_data$area_m2)
  area_min <- min(crop_data$area_m2)
  area_max <- max(crop_data$area_m2)
  area_median <- median(crop_data$area_m2)
  
  cat(sprintf("  Média:           %.2f m²\n", area_mean))
  cat(sprintf("  Desvio Padrão:   %.2f m²\n", area_sd))
  cat(sprintf("  Mediana:         %.2f m²\n", area_median))
  cat(sprintf("  Mínimo:          %.2f m²\n", area_min))
  cat(sprintf("  Máximo:          %.2f m²\n", area_max))
  cat(sprintf("  Variância:       %.2f\n", var(crop_data$area_m2)))
  
  print_header("Estatísticas - Número de Ruas")
  
  rows_mean <- mean(crop_data$rows)
  rows_sd <- sd(crop_data$rows)
  rows_min <- min(crop_data$rows)
  rows_max <- max(crop_data$rows)
  rows_median <- median(crop_data$rows)
  
  cat(sprintf("  Média:           %.2f ruas\n", rows_mean))
  cat(sprintf("  Desvio Padrão:   %.2f ruas\n", rows_sd))
  cat(sprintf("  Mediana:         %.0f ruas\n", rows_median))
  cat(sprintf("  Mínimo:          %d ruas\n", rows_min))
  cat(sprintf("  Máximo:          %d ruas\n", rows_max))
  
  print_header("Estatísticas - Quantidade de Insumo (mL/m)")
  
  input_mean <- mean(crop_data$input_amount_ml_per_m)
  input_sd <- sd(crop_data$input_amount_ml_per_m)
  input_min <- min(crop_data$input_amount_ml_per_m)
  input_max <- max(crop_data$input_amount_ml_per_m)
  input_median <- median(crop_data$input_amount_ml_per_m)
  
  cat(sprintf("  Média:           %.2f mL/m\n", input_mean))
  cat(sprintf("  Desvio Padrão:   %.2f mL/m\n", input_sd))
  cat(sprintf("  Mediana:         %.2f mL/m\n", input_median))
  cat(sprintf("  Mínimo:          %.2f mL/m\n", input_min))
  cat(sprintf("  Máximo:          %.2f mL/m\n", input_max))
  
  print_header("Estatísticas por Tipo de Cultura")
  
  crop_types <- unique(crop_data$crop_type)
  
  for (crop in crop_types) {
    crop_subset <- subset(crop_data, crop_type == crop)
    
    cat("\n", crop, "\n")
    print_divider()
    cat(sprintf("  Quantidade de registros: %d\n", nrow(crop_subset)))
    cat(sprintf("  Área média:              %.2f m²\n", mean(crop_subset$area_m2)))
    cat(sprintf("  Desvio padrão (área):    %.2f m²\n", sd(crop_subset$area_m2)))
    cat(sprintf("  Média de ruas:           %.2f\n", mean(crop_subset$rows)))
    cat(sprintf("  Insumo médio:            %.2f mL/m\n", mean(crop_subset$input_amount_ml_per_m)))
    cat("\n")
  }
  
  print_header("Insights Adicionais")
  
  total_area <- sum(crop_data$area_m2)
  cat(sprintf("  Área total cultivada:    %.2f m² (%.2f hectares)\n", 
              total_area, total_area / 10000))
  
  avg_area_by_crop <- aggregate(area_m2 ~ crop_type, data = crop_data, FUN = mean)
  largest_crop <- avg_area_by_crop[which.max(avg_area_by_crop$area_m2), ]
  cat(sprintf("  Cultura com maior área média: %s (%.2f m²)\n", 
              largest_crop$crop_type, largest_crop$area_m2))
  
  cat("\n")
  print_divider()
  cat("Análise concluída com sucesso!\n")
  print_divider()
  cat("\n")
}

tryCatch({
  main()
}, error = function(e) {
  cat("\n ERRO durante a análise:\n")
  cat(conditionMessage(e), "\n\n")
})
