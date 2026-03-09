echo ""
echo "============================================================================"
echo "  FarmTech Solutions - Verificação de Dependências"
echo "============================================================================"
echo ""

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' 

check_command() {
    if command -v $1 &> /dev/null; then
        VERSION=$($1 --version 2>&1 | head -n 1)
        echo -e "${GREEN}✓${NC} $2 está instalado: $VERSION"
        return 0
    else
        echo -e "${RED}✗${NC} $2 NÃO está instalado"
        echo -e "   ${YELLOW}→${NC} Instale em: $3"
        return 1
    fi
}

echo "Verificando Python..."
if command -v python3 &> /dev/null; then
    check_command python3 "Python" "https://www.python.org/downloads/"
elif command -v python &> /dev/null; then
    check_command python "Python" "https://www.python.org/downloads/"
else
    echo -e "${RED}✗${NC} Python NÃO está instalado"
    echo -e "   ${YELLOW}→${NC} Instale em: https://www.python.org/downloads/"
fi

echo ""

echo "Verificando R..."
check_command Rscript "R" "https://cran.r-project.org/"

echo ""

echo "Verificando Git..."
check_command git "Git" "https://git-scm.com/downloads"

echo ""
echo "============================================================================"
echo "  Verificação de Estrutura de Arquivos"
echo "============================================================================"
echo ""

# Check file structure
FILES=(
    "src/python/main.py"
    "src/r/statistics_analysis.R"
    "src/r/weather_api.R"
    "README.md"
    "QUICK_START.md"
    "GIT_GUIDE.md"
    "CHECKLIST.md"
    ".gitignore"
    "docs/article_summary.md"
    "docs/video_link.txt"
)

for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}✓${NC} $file"
    else
        echo -e "${RED}✗${NC} $file não encontrado"
    fi
done

echo ""
echo "============================================================================"
echo "  Próximos Passos"
echo "============================================================================"
echo ""
echo "1. Se algo não está instalado, siga as instruções acima"
echo "2. Leia o QUICK_START.md para começar rapidamente"
echo "3. Leia o README.md para instruções completas"
echo "4. Leia o GIT_GUIDE.md para usar Git e GitHub"
echo ""
echo "Para executar o projeto:"
echo "  cd src/python && python3 main.py"
echo ""
echo "============================================================================"
echo ""
