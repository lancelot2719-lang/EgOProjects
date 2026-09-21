#!/bin/bash
set -e
cd ~/mnt/Книги
mkdir -p 'свободные_книги/_move_log'
LOG=свободные_книги/_move_log/move_20260920.log
: > "$LOG"
if [ -e 'Финансы/01_wealth_of_nations_adam_smith.pdf' ]; then
  echo "SKIP(exists): 01_wealth_of_nations_adam_smith.pdf -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/01_wealth_of_nations_adam_smith.pdf' 'Финансы/01_wealth_of_nations_adam_smith.pdf' && echo "MOVED: 01_wealth_of_nations_adam_smith.pdf -> Финансы" >> "$LOG" || echo "FAIL: 01_wealth_of_nations_adam_smith.pdf -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/01_wealth_of_nations_analysis.md' ]; then
  echo "SKIP(exists): 01_wealth_of_nations_analysis.md -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/01_wealth_of_nations_analysis.md' 'Финансы/01_wealth_of_nations_analysis.md' && echo "MOVED: 01_wealth_of_nations_analysis.md -> Финансы" >> "$LOG" || echo "FAIL: 01_wealth_of_nations_analysis.md -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/02_reminiscences_stock_operator_lefevre.pdf' ]; then
  echo "SKIP(exists): 02_reminiscences_stock_operator_lefevre.pdf -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/02_reminiscences_stock_operator_lefevre.pdf' 'Финансы/02_reminiscences_stock_operator_lefevre.pdf' && echo "MOVED: 02_reminiscences_stock_operator_lefevre.pdf -> Финансы" >> "$LOG" || echo "FAIL: 02_reminiscences_stock_operator_lefevre.pdf -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/02_stock_operator_analysis.md' ]; then
  echo "SKIP(exists): 02_stock_operator_analysis.md -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/02_stock_operator_analysis.md' 'Финансы/02_stock_operator_analysis.md' && echo "MOVED: 02_stock_operator_analysis.md -> Финансы" >> "$LOG" || echo "FAIL: 02_stock_operator_analysis.md -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/03_economic_consequences_of_peace_keynes.pdf' ]; then
  echo "SKIP(exists): 03_economic_consequences_of_peace_keynes.pdf -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/03_economic_consequences_of_peace_keynes.pdf' 'Финансы/03_economic_consequences_of_peace_keynes.pdf' && echo "MOVED: 03_economic_consequences_of_peace_keynes.pdf -> Финансы" >> "$LOG" || echo "FAIL: 03_economic_consequences_of_peace_keynes.pdf -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/03_economic_consequences_peace_analysis.md' ]; then
  echo "SKIP(exists): 03_economic_consequences_peace_analysis.md -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/03_economic_consequences_peace_analysis.md' 'Финансы/03_economic_consequences_peace_analysis.md' && echo "MOVED: 03_economic_consequences_peace_analysis.md -> Финансы" >> "$LOG" || echo "FAIL: 03_economic_consequences_peace_analysis.md -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/04_lombard_street_analysis.md' ]; then
  echo "SKIP(exists): 04_lombard_street_analysis.md -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/04_lombard_street_analysis.md' 'Финансы/04_lombard_street_analysis.md' && echo "MOVED: 04_lombard_street_analysis.md -> Финансы" >> "$LOG" || echo "FAIL: 04_lombard_street_analysis.md -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/04_lombard_street_bagehot.pdf' ]; then
  echo "SKIP(exists): 04_lombard_street_bagehot.pdf -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/04_lombard_street_bagehot.pdf' 'Финансы/04_lombard_street_bagehot.pdf' && echo "MOVED: 04_lombard_street_bagehot.pdf -> Финансы" >> "$LOG" || echo "FAIL: 04_lombard_street_bagehot.pdf -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/05_other_peoples_money_analysis.md' ]; then
  echo "SKIP(exists): 05_other_peoples_money_analysis.md -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/05_other_peoples_money_analysis.md' 'Финансы/05_other_peoples_money_analysis.md' && echo "MOVED: 05_other_peoples_money_analysis.md -> Финансы" >> "$LOG" || echo "FAIL: 05_other_peoples_money_analysis.md -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/05_other_peoples_money_brandeis.pdf' ]; then
  echo "SKIP(exists): 05_other_peoples_money_brandeis.pdf -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/05_other_peoples_money_brandeis.pdf' 'Финансы/05_other_peoples_money_brandeis.pdf' && echo "MOVED: 05_other_peoples_money_brandeis.pdf -> Финансы" >> "$LOG" || echo "FAIL: 05_other_peoples_money_brandeis.pdf -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/06_fifty_years_wall_street_analysis.md' ]; then
  echo "SKIP(exists): 06_fifty_years_wall_street_analysis.md -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/06_fifty_years_wall_street_analysis.md' 'Финансы/06_fifty_years_wall_street_analysis.md' && echo "MOVED: 06_fifty_years_wall_street_analysis.md -> Финансы" >> "$LOG" || echo "FAIL: 06_fifty_years_wall_street_analysis.md -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/06_fifty_years_wall_street_clews.pdf' ]; then
  echo "SKIP(exists): 06_fifty_years_wall_street_clews.pdf -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/06_fifty_years_wall_street_clews.pdf' 'Финансы/06_fifty_years_wall_street_clews.pdf' && echo "MOVED: 06_fifty_years_wall_street_clews.pdf -> Финансы" >> "$LOG" || echo "FAIL: 06_fifty_years_wall_street_clews.pdf -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/07_random_reminiscences_analysis.md' ]; then
  echo "SKIP(exists): 07_random_reminiscences_analysis.md -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/07_random_reminiscences_analysis.md' 'Финансы/07_random_reminiscences_analysis.md' && echo "MOVED: 07_random_reminiscences_analysis.md -> Финансы" >> "$LOG" || echo "FAIL: 07_random_reminiscences_analysis.md -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/07_random_reminiscences_rockefeller.pdf' ]; then
  echo "SKIP(exists): 07_random_reminiscences_rockefeller.pdf -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/07_random_reminiscences_rockefeller.pdf' 'Финансы/07_random_reminiscences_rockefeller.pdf' && echo "MOVED: 07_random_reminiscences_rockefeller.pdf -> Финансы" >> "$LOG" || echo "FAIL: 07_random_reminiscences_rockefeller.pdf -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/08_art_of_money_getting_analysis.md' ]; then
  echo "SKIP(exists): 08_art_of_money_getting_analysis.md -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/08_art_of_money_getting_analysis.md' 'Финансы/08_art_of_money_getting_analysis.md' && echo "MOVED: 08_art_of_money_getting_analysis.md -> Финансы" >> "$LOG" || echo "FAIL: 08_art_of_money_getting_analysis.md -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/08_art_of_money_getting_barnum.pdf' ]; then
  echo "SKIP(exists): 08_art_of_money_getting_barnum.pdf -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/08_art_of_money_getting_barnum.pdf' 'Финансы/08_art_of_money_getting_barnum.pdf' && echo "MOVED: 08_art_of_money_getting_barnum.pdf -> Финансы" >> "$LOG" || echo "FAIL: 08_art_of_money_getting_barnum.pdf -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/09_how_to_invest_money_analysis.md' ]; then
  echo "SKIP(exists): 09_how_to_invest_money_analysis.md -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/09_how_to_invest_money_analysis.md' 'Финансы/09_how_to_invest_money_analysis.md' && echo "MOVED: 09_how_to_invest_money_analysis.md -> Финансы" >> "$LOG" || echo "FAIL: 09_how_to_invest_money_analysis.md -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/09_how_to_invest_money_henry.pdf' ]; then
  echo "SKIP(exists): 09_how_to_invest_money_henry.pdf -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/09_how_to_invest_money_henry.pdf' 'Финансы/09_how_to_invest_money_henry.pdf' && echo "MOVED: 09_how_to_invest_money_henry.pdf -> Финансы" >> "$LOG" || echo "FAIL: 09_how_to_invest_money_henry.pdf -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/10_tract_on_monetary_reform_analysis.md' ]; then
  echo "SKIP(exists): 10_tract_on_monetary_reform_analysis.md -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/10_tract_on_monetary_reform_analysis.md' 'Финансы/10_tract_on_monetary_reform_analysis.md' && echo "MOVED: 10_tract_on_monetary_reform_analysis.md -> Финансы" >> "$LOG" || echo "FAIL: 10_tract_on_monetary_reform_analysis.md -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/10_tract_on_monetary_reform_keynes.pdf' ]; then
  echo "SKIP(exists): 10_tract_on_monetary_reform_keynes.pdf -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/10_tract_on_monetary_reform_keynes.pdf' 'Финансы/10_tract_on_monetary_reform_keynes.pdf' && echo "MOVED: 10_tract_on_monetary_reform_keynes.pdf -> Финансы" >> "$LOG" || echo "FAIL: 10_tract_on_monetary_reform_keynes.pdf -> Финансы" >> "$LOG"
fi
if [ -e 'Психология/12 правил жизни. Противоядие от хаоса - часть 1.txt' ]; then
  echo "SKIP(exists): 12 правил жизни. Противоядие от хаоса - часть 1.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/12 правил жизни. Противоядие от хаоса - часть 1.txt' 'Психология/12 правил жизни. Противоядие от хаоса - часть 1.txt' && echo "MOVED: 12 правил жизни. Противоядие от хаоса - часть 1.txt -> Психология" >> "$LOG" || echo "FAIL: 12 правил жизни. Противоядие от хаоса - часть 1.txt -> Психология" >> "$LOG"
fi
if [ -e 'Психология/12 правил жизни. Противоядие от хаоса - часть 2.txt' ]; then
  echo "SKIP(exists): 12 правил жизни. Противоядие от хаоса - часть 2.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/12 правил жизни. Противоядие от хаоса - часть 2.txt' 'Психология/12 правил жизни. Противоядие от хаоса - часть 2.txt' && echo "MOVED: 12 правил жизни. Противоядие от хаоса - часть 2.txt -> Психология" >> "$LOG" || echo "FAIL: 12 правил жизни. Противоядие от хаоса - часть 2.txt -> Психология" >> "$LOG"
fi
if [ -e 'Тайм-менеджмент/12_недель_в_году.txt' ]; then
  echo "SKIP(exists): 12_недель_в_году.txt -> Тайм-менеджмент" >> "$LOG"
else
  mv 'свободные_книги/12_недель_в_году.txt' 'Тайм-менеджмент/12_недель_в_году.txt' && echo "MOVED: 12_недель_в_году.txt -> Тайм-менеджмент" >> "$LOG" || echo "FAIL: 12_недель_в_году.txt -> Тайм-менеджмент" >> "$LOG"
fi
if [ -e 'Развитие/21_урок_для_XXI_века.txt' ]; then
  echo "SKIP(exists): 21_урок_для_XXI_века.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/21_урок_для_XXI_века.txt' 'Развитие/21_урок_для_XXI_века.txt' && echo "MOVED: 21_урок_для_XXI_века.txt -> Развитие" >> "$LOG" || echo "FAIL: 21_урок_для_XXI_века.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/21_урок_для_XXI_века2.txt' ]; then
  echo "SKIP(exists): 21_урок_для_XXI_века2.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/21_урок_для_XXI_века2.txt' 'Развитие/21_урок_для_XXI_века2.txt' && echo "MOVED: 21_урок_для_XXI_века2.txt -> Развитие" >> "$LOG" || echo "FAIL: 21_урок_для_XXI_века2.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/7 навыков высокоффективных людей.txt' ]; then
  echo "SKIP(exists): 7 навыков высокоффективных людей.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/7 навыков высокоффективных людей.txt' 'Развитие/7 навыков высокоффективных людей.txt' && echo "MOVED: 7 навыков высокоффективных людей.txt -> Развитие" >> "$LOG" || echo "FAIL: 7 навыков высокоффективных людей.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Продажи/Afanaseva_Prodavay-kak-bog-Vklyuchit-sumasshedshuyu-konversiyu.vEuqUw.610688.fb2' ]; then
  echo "SKIP(exists): Afanaseva_Prodavay-kak-bog-Vklyuchit-sumasshedshuyu-konversiyu.vEuqUw.610688.fb2 -> Продажи" >> "$LOG"
else
  mv 'свободные_книги/Afanaseva_Prodavay-kak-bog-Vklyuchit-sumasshedshuyu-konversiyu.vEuqUw.610688.fb2' 'Продажи/Afanaseva_Prodavay-kak-bog-Vklyuchit-sumasshedshuyu-konversiyu.vEuqUw.610688.fb2' && echo "MOVED: Afanaseva_Prodavay-kak-bog-Vklyuchit-sumasshedshuyu-konversiyu.vEuqUw.610688.fb2 -> Продажи" >> "$LOG" || echo "FAIL: Afanaseva_Prodavay-kak-bog-Vklyuchit-sumasshedshuyu-konversiyu.vEuqUw.610688.fb2 -> Продажи" >> "$LOG"
fi
if [ -e 'Продажи/Afanaseva_Prodavay-kak-bog-Vklyuchit-sumasshedshuyu-konversiyu.vEuqUw.610688.txt' ]; then
  echo "SKIP(exists): Afanaseva_Prodavay-kak-bog-Vklyuchit-sumasshedshuyu-konversiyu.vEuqUw.610688.txt -> Продажи" >> "$LOG"
else
  mv 'свободные_книги/Afanaseva_Prodavay-kak-bog-Vklyuchit-sumasshedshuyu-konversiyu.vEuqUw.610688.txt' 'Продажи/Afanaseva_Prodavay-kak-bog-Vklyuchit-sumasshedshuyu-konversiyu.vEuqUw.610688.txt' && echo "MOVED: Afanaseva_Prodavay-kak-bog-Vklyuchit-sumasshedshuyu-konversiyu.vEuqUw.610688.txt -> Продажи" >> "$LOG" || echo "FAIL: Afanaseva_Prodavay-kak-bog-Vklyuchit-sumasshedshuyu-konversiyu.vEuqUw.610688.txt -> Продажи" >> "$LOG"
fi
if [ -e 'Развитие/Alekseev_Chto-Gde-Kogda-.cAZJrQ.114741.txt' ]; then
  echo "SKIP(exists): Alekseev_Chto-Gde-Kogda-.cAZJrQ.114741.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Alekseev_Chto-Gde-Kogda-.cAZJrQ.114741.txt' 'Развитие/Alekseev_Chto-Gde-Kogda-.cAZJrQ.114741.txt' && echo "MOVED: Alekseev_Chto-Gde-Kogda-.cAZJrQ.114741.txt -> Развитие" >> "$LOG" || echo "FAIL: Alekseev_Chto-Gde-Kogda-.cAZJrQ.114741.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Тайм-менеджмент/Allen_Kak-privesti-dela-v-poryadok.K8h6qg.182172.fb2' ]; then
  echo "SKIP(exists): Allen_Kak-privesti-dela-v-poryadok.K8h6qg.182172.fb2 -> Тайм-менеджмент" >> "$LOG"
else
  mv 'свободные_книги/Allen_Kak-privesti-dela-v-poryadok.K8h6qg.182172.fb2' 'Тайм-менеджмент/Allen_Kak-privesti-dela-v-poryadok.K8h6qg.182172.fb2' && echo "MOVED: Allen_Kak-privesti-dela-v-poryadok.K8h6qg.182172.fb2 -> Тайм-менеджмент" >> "$LOG" || echo "FAIL: Allen_Kak-privesti-dela-v-poryadok.K8h6qg.182172.fb2 -> Тайм-менеджмент" >> "$LOG"
fi
if [ -e 'Развитие/Arieli_Predskazuemaya-irracionalnost-Skrytye-sily-opredelyayushchie-nashi-resheniya.pssCNQ.350343.txt' ]; then
  echo "SKIP(exists): Arieli_Predskazuemaya-irracionalnost-Skrytye-sily-opredelyayushchie-nashi-resheniya.pssCNQ.350343.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Arieli_Predskazuemaya-irracionalnost-Skrytye-sily-opredelyayushchie-nashi-resheniya.pssCNQ.350343.txt' 'Развитие/Arieli_Predskazuemaya-irracionalnost-Skrytye-sily-opredelyayushchie-nashi-resheniya.pssCNQ.350343.txt' && echo "MOVED: Arieli_Predskazuemaya-irracionalnost-Skrytye-sily-opredelyayushchie-nashi-resheniya.pssCNQ.350343.txt -> Развитие" >> "$LOG" || echo "FAIL: Arieli_Predskazuemaya-irracionalnost-Skrytye-sily-opredelyayushchie-nashi-resheniya.pssCNQ.350343.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Психология/Barnard_Pitanie-dlya-mozga-Effektivnaya-poshagovaya-metodika-dlya-usileniya-effektivnosti-raboty-moz.txt' ]; then
  echo "SKIP(exists): Barnard_Pitanie-dlya-mozga-Effektivnaya-poshagovaya-metodika-dlya-usileniya-effektivnosti-raboty-moz.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Barnard_Pitanie-dlya-mozga-Effektivnaya-poshagovaya-metodika-dlya-usileniya-effektivnosti-raboty-moz.txt' 'Психология/Barnard_Pitanie-dlya-mozga-Effektivnaya-poshagovaya-metodika-dlya-usileniya-effektivnosti-raboty-moz.txt' && echo "MOVED: Barnard_Pitanie-dlya-mozga-Effektivnaya-poshagovaya-metodika-dlya-usileniya-effektivnosti-raboty-moz.txt -> Психология" >> "$LOG" || echo "FAIL: Barnard_Pitanie-dlya-mozga-Effektivnaya-poshagovaya-metodika-dlya-usileniya-effektivnosti-raboty-moz.txt -> Психология" >> "$LOG"
fi
if [ -e 'Продажи/Barysheva_Kak-prodat-slona-ili-51-priem-zaklyucheniya-sdelki.-iLJ_A.304248.fb2' ]; then
  echo "SKIP(exists): Barysheva_Kak-prodat-slona-ili-51-priem-zaklyucheniya-sdelki.-iLJ_A.304248.fb2 -> Продажи" >> "$LOG"
else
  mv 'свободные_книги/Barysheva_Kak-prodat-slona-ili-51-priem-zaklyucheniya-sdelki.-iLJ_A.304248.fb2' 'Продажи/Barysheva_Kak-prodat-slona-ili-51-priem-zaklyucheniya-sdelki.-iLJ_A.304248.fb2' && echo "MOVED: Barysheva_Kak-prodat-slona-ili-51-priem-zaklyucheniya-sdelki.-iLJ_A.304248.fb2 -> Продажи" >> "$LOG" || echo "FAIL: Barysheva_Kak-prodat-slona-ili-51-priem-zaklyucheniya-sdelki.-iLJ_A.304248.fb2 -> Продажи" >> "$LOG"
fi
if [ -e 'Продажи/Barysheva_Kak-prodat-slona-ili-51-priem-zaklyucheniya-sdelki.-iLJ_A.304248.txt' ]; then
  echo "SKIP(exists): Barysheva_Kak-prodat-slona-ili-51-priem-zaklyucheniya-sdelki.-iLJ_A.304248.txt -> Продажи" >> "$LOG"
else
  mv 'свободные_книги/Barysheva_Kak-prodat-slona-ili-51-priem-zaklyucheniya-sdelki.-iLJ_A.304248.txt' 'Продажи/Barysheva_Kak-prodat-slona-ili-51-priem-zaklyucheniya-sdelki.-iLJ_A.304248.txt' && echo "MOVED: Barysheva_Kak-prodat-slona-ili-51-priem-zaklyucheniya-sdelki.-iLJ_A.304248.txt -> Продажи" >> "$LOG" || echo "FAIL: Barysheva_Kak-prodat-slona-ili-51-priem-zaklyucheniya-sdelki.-iLJ_A.304248.txt -> Продажи" >> "$LOG"
fi
if [ -e 'Общение, красноречие, голос/Bredemayer_Chernaya-ritorika-Vlast-i-magiya-slova.V-wvWA.479351.txt' ]; then
  echo "SKIP(exists): Bredemayer_Chernaya-ritorika-Vlast-i-magiya-slova.V-wvWA.479351.txt -> Общение, красноречие, голос" >> "$LOG"
else
  mv 'свободные_книги/Bredemayer_Chernaya-ritorika-Vlast-i-magiya-slova.V-wvWA.479351.txt' 'Общение, красноречие, голос/Bredemayer_Chernaya-ritorika-Vlast-i-magiya-slova.V-wvWA.479351.txt' && echo "MOVED: Bredemayer_Chernaya-ritorika-Vlast-i-magiya-slova.V-wvWA.479351.txt -> Общение, красноречие, голос" >> "$LOG" || echo "FAIL: Bredemayer_Chernaya-ritorika-Vlast-i-magiya-slova.V-wvWA.479351.txt -> Общение, красноречие, голос" >> "$LOG"
fi
if [ -e 'Продажи/Chaldini_Psihologiya-ubezhdeniya-60-dokazannyh-sposobov-byt-ubeditelnym.q6zXKw.691573.txt' ]; then
  echo "SKIP(exists): Chaldini_Psihologiya-ubezhdeniya-60-dokazannyh-sposobov-byt-ubeditelnym.q6zXKw.691573.txt -> Продажи" >> "$LOG"
else
  mv 'свободные_книги/Chaldini_Psihologiya-ubezhdeniya-60-dokazannyh-sposobov-byt-ubeditelnym.q6zXKw.691573.txt' 'Продажи/Chaldini_Psihologiya-ubezhdeniya-60-dokazannyh-sposobov-byt-ubeditelnym.q6zXKw.691573.txt' && echo "MOVED: Chaldini_Psihologiya-ubezhdeniya-60-dokazannyh-sposobov-byt-ubeditelnym.q6zXKw.691573.txt -> Продажи" >> "$LOG" || echo "FAIL: Chaldini_Psihologiya-ubezhdeniya-60-dokazannyh-sposobov-byt-ubeditelnym.q6zXKw.691573.txt -> Продажи" >> "$LOG"
fi
if [ -e 'Продажи/Chaldini_Psihologiya-ubezhdeniya-Vazhnye-melochi-garantiruyushchie-uspeh.Hihx-Q.429971.txt' ]; then
  echo "SKIP(exists): Chaldini_Psihologiya-ubezhdeniya-Vazhnye-melochi-garantiruyushchie-uspeh.Hihx-Q.429971.txt -> Продажи" >> "$LOG"
else
  mv 'свободные_книги/Chaldini_Psihologiya-ubezhdeniya-Vazhnye-melochi-garantiruyushchie-uspeh.Hihx-Q.429971.txt' 'Продажи/Chaldini_Psihologiya-ubezhdeniya-Vazhnye-melochi-garantiruyushchie-uspeh.Hihx-Q.429971.txt' && echo "MOVED: Chaldini_Psihologiya-ubezhdeniya-Vazhnye-melochi-garantiruyushchie-uspeh.Hihx-Q.429971.txt -> Продажи" >> "$LOG" || echo "FAIL: Chaldini_Psihologiya-ubezhdeniya-Vazhnye-melochi-garantiruyushchie-uspeh.Hihx-Q.429971.txt -> Продажи" >> "$LOG"
fi
if [ -e 'Психология/Devidson_Emocionalnaya-zhizn-mozga.NQzUvQ.494631.txt' ]; then
  echo "SKIP(exists): Devidson_Emocionalnaya-zhizn-mozga.NQzUvQ.494631.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Devidson_Emocionalnaya-zhizn-mozga.NQzUvQ.494631.txt' 'Психология/Devidson_Emocionalnaya-zhizn-mozga.NQzUvQ.494631.txt' && echo "MOVED: Devidson_Emocionalnaya-zhizn-mozga.NQzUvQ.494631.txt -> Психология" >> "$LOG" || echo "FAIL: Devidson_Emocionalnaya-zhizn-mozga.NQzUvQ.494631.txt -> Психология" >> "$LOG"
fi
if [ -e 'Тайм-менеджмент/Dzhonson_52-ponedelnika-Kak-za-god-dobitsya-lyubyh-celey.EkcKBQ.423742.fb2' ]; then
  echo "SKIP(exists): Dzhonson_52-ponedelnika-Kak-za-god-dobitsya-lyubyh-celey.EkcKBQ.423742.fb2 -> Тайм-менеджмент" >> "$LOG"
else
  mv 'свободные_книги/Dzhonson_52-ponedelnika-Kak-za-god-dobitsya-lyubyh-celey.EkcKBQ.423742.fb2' 'Тайм-менеджмент/Dzhonson_52-ponedelnika-Kak-za-god-dobitsya-lyubyh-celey.EkcKBQ.423742.fb2' && echo "MOVED: Dzhonson_52-ponedelnika-Kak-za-god-dobitsya-lyubyh-celey.EkcKBQ.423742.fb2 -> Тайм-менеджмент" >> "$LOG" || echo "FAIL: Dzhonson_52-ponedelnika-Kak-za-god-dobitsya-lyubyh-celey.EkcKBQ.423742.fb2 -> Тайм-менеджмент" >> "$LOG"
fi
if [ -e 'Тайм-менеджмент/Dzhonson_52-ponedelnika-Kak-za-god-dobitsya-lyubyh-celey.EkcKBQ.423742.txt' ]; then
  echo "SKIP(exists): Dzhonson_52-ponedelnika-Kak-za-god-dobitsya-lyubyh-celey.EkcKBQ.423742.txt -> Тайм-менеджмент" >> "$LOG"
else
  mv 'свободные_книги/Dzhonson_52-ponedelnika-Kak-za-god-dobitsya-lyubyh-celey.EkcKBQ.423742.txt' 'Тайм-менеджмент/Dzhonson_52-ponedelnika-Kak-za-god-dobitsya-lyubyh-celey.EkcKBQ.423742.txt' && echo "MOVED: Dzhonson_52-ponedelnika-Kak-za-god-dobitsya-lyubyh-celey.EkcKBQ.423742.txt -> Тайм-менеджмент" >> "$LOG" || echo "FAIL: Dzhonson_52-ponedelnika-Kak-za-god-dobitsya-lyubyh-celey.EkcKBQ.423742.txt -> Тайм-менеджмент" >> "$LOG"
fi
if [ -e 'Тайм-менеджмент/Ferriss_Kak-rabotat-po-4-chasa-v-nedelyu-i-pri-etom-ne-torchat-v-ofise-ot-zvonka-do-zvonka-zhit-gde-.txt' ]; then
  echo "SKIP(exists): Ferriss_Kak-rabotat-po-4-chasa-v-nedelyu-i-pri-etom-ne-torchat-v-ofise-ot-zvonka-do-zvonka-zhit-gde-.txt -> Тайм-менеджмент" >> "$LOG"
else
  mv 'свободные_книги/Ferriss_Kak-rabotat-po-4-chasa-v-nedelyu-i-pri-etom-ne-torchat-v-ofise-ot-zvonka-do-zvonka-zhit-gde-.txt' 'Тайм-менеджмент/Ferriss_Kak-rabotat-po-4-chasa-v-nedelyu-i-pri-etom-ne-torchat-v-ofise-ot-zvonka-do-zvonka-zhit-gde-.txt' && echo "MOVED: Ferriss_Kak-rabotat-po-4-chasa-v-nedelyu-i-pri-etom-ne-torchat-v-ofise-ot-zvonka-do-zvonka-zhit-gde-.txt -> Тайм-менеджмент" >> "$LOG" || echo "FAIL: Ferriss_Kak-rabotat-po-4-chasa-v-nedelyu-i-pri-etom-ne-torchat-v-ofise-ot-zvonka-do-zvonka-zhit-gde-.txt -> Тайм-менеджмент" >> "$LOG"
fi
if [ -e 'Тайм-менеджмент/Ferriss_Kak-rabotat-po-4-chasa-v-nedelyu-i-pri-etom-ne-torchat-v-ofise-ot-zvonka-do-zvonka-zhit-gde-ugodno-i-bogatet.-JXe_Q.292920.fb2' ]; then
  echo "SKIP(exists): Ferriss_Kak-rabotat-po-4-chasa-v-nedelyu-i-pri-etom-ne-torchat-v-ofise-ot-zvonka-do-zvonka-zhit-gde-ugodno-i-bogatet.-JXe_Q.292920.fb2 -> Тайм-менеджмент" >> "$LOG"
else
  mv 'свободные_книги/Ferriss_Kak-rabotat-po-4-chasa-v-nedelyu-i-pri-etom-ne-torchat-v-ofise-ot-zvonka-do-zvonka-zhit-gde-ugodno-i-bogatet.-JXe_Q.292920.fb2' 'Тайм-менеджмент/Ferriss_Kak-rabotat-po-4-chasa-v-nedelyu-i-pri-etom-ne-torchat-v-ofise-ot-zvonka-do-zvonka-zhit-gde-ugodno-i-bogatet.-JXe_Q.292920.fb2' && echo "MOVED: Ferriss_Kak-rabotat-po-4-chasa-v-nedelyu-i-pri-etom-ne-torchat-v-ofise-ot-zvonka-do-zvonka-zhit-gde-ugodno-i-bogatet.-JXe_Q.292920.fb2 -> Тайм-менеджмент" >> "$LOG" || echo "FAIL: Ferriss_Kak-rabotat-po-4-chasa-v-nedelyu-i-pri-etom-ne-torchat-v-ofise-ot-zvonka-do-zvonka-zhit-gde-ugodno-i-bogatet.-JXe_Q.292920.fb2 -> Тайм-менеджмент" >> "$LOG"
fi
if [ -e 'Тайм-менеджмент/Fridman_Pozhirateli-vremeni-Kak-izbavit-ot-lishney-raboty-sebya-i-sotrudnikov.Adu-oQ.557080.fb2' ]; then
  echo "SKIP(exists): Fridman_Pozhirateli-vremeni-Kak-izbavit-ot-lishney-raboty-sebya-i-sotrudnikov.Adu-oQ.557080.fb2 -> Тайм-менеджмент" >> "$LOG"
else
  mv 'свободные_книги/Fridman_Pozhirateli-vremeni-Kak-izbavit-ot-lishney-raboty-sebya-i-sotrudnikov.Adu-oQ.557080.fb2' 'Тайм-менеджмент/Fridman_Pozhirateli-vremeni-Kak-izbavit-ot-lishney-raboty-sebya-i-sotrudnikov.Adu-oQ.557080.fb2' && echo "MOVED: Fridman_Pozhirateli-vremeni-Kak-izbavit-ot-lishney-raboty-sebya-i-sotrudnikov.Adu-oQ.557080.fb2 -> Тайм-менеджмент" >> "$LOG" || echo "FAIL: Fridman_Pozhirateli-vremeni-Kak-izbavit-ot-lishney-raboty-sebya-i-sotrudnikov.Adu-oQ.557080.fb2 -> Тайм-менеджмент" >> "$LOG"
fi
if [ -e 'Тайм-менеджмент/Fridman_Pozhirateli-vremeni-Kak-izbavit-ot-lishney-raboty-sebya-i-sotrudnikov.Adu-oQ.557080.txt' ]; then
  echo "SKIP(exists): Fridman_Pozhirateli-vremeni-Kak-izbavit-ot-lishney-raboty-sebya-i-sotrudnikov.Adu-oQ.557080.txt -> Тайм-менеджмент" >> "$LOG"
else
  mv 'свободные_книги/Fridman_Pozhirateli-vremeni-Kak-izbavit-ot-lishney-raboty-sebya-i-sotrudnikov.Adu-oQ.557080.txt' 'Тайм-менеджмент/Fridman_Pozhirateli-vremeni-Kak-izbavit-ot-lishney-raboty-sebya-i-sotrudnikov.Adu-oQ.557080.txt' && echo "MOVED: Fridman_Pozhirateli-vremeni-Kak-izbavit-ot-lishney-raboty-sebya-i-sotrudnikov.Adu-oQ.557080.txt -> Тайм-менеджмент" >> "$LOG" || echo "FAIL: Fridman_Pozhirateli-vremeni-Kak-izbavit-ot-lishney-raboty-sebya-i-sotrudnikov.Adu-oQ.557080.txt -> Тайм-менеджмент" >> "$LOG"
fi
if [ -e 'Финансы/Geydzh_Pochemu-vy-glupy-bolny-i-bedny-I-kak-stat-umnym-zdorovym-i-bogatym-.6kmuvA.93457.txt' ]; then
  echo "SKIP(exists): Geydzh_Pochemu-vy-glupy-bolny-i-bedny-I-kak-stat-umnym-zdorovym-i-bogatym-.6kmuvA.93457.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Geydzh_Pochemu-vy-glupy-bolny-i-bedny-I-kak-stat-umnym-zdorovym-i-bogatym-.6kmuvA.93457.txt' 'Финансы/Geydzh_Pochemu-vy-glupy-bolny-i-bedny-I-kak-stat-umnym-zdorovym-i-bogatym-.6kmuvA.93457.txt' && echo "MOVED: Geydzh_Pochemu-vy-glupy-bolny-i-bedny-I-kak-stat-umnym-zdorovym-i-bogatym-.6kmuvA.93457.txt -> Финансы" >> "$LOG" || echo "FAIL: Geydzh_Pochemu-vy-glupy-bolny-i-bedny-I-kak-stat-umnym-zdorovym-i-bogatym-.6kmuvA.93457.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Развитие/Granin_Eta-strannaya-zhizn.06lpZg.239869.txt' ]; then
  echo "SKIP(exists): Granin_Eta-strannaya-zhizn.06lpZg.239869.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Granin_Eta-strannaya-zhizn.06lpZg.239869.txt' 'Развитие/Granin_Eta-strannaya-zhizn.06lpZg.239869.txt' && echo "MOVED: Granin_Eta-strannaya-zhizn.06lpZg.239869.txt -> Развитие" >> "$LOG" || echo "FAIL: Granin_Eta-strannaya-zhizn.06lpZg.239869.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Grant_Podumayte-eshche-raz-Sila-znaniya-o-neznanii.qEuXZQ.640589.txt' ]; then
  echo "SKIP(exists): Grant_Podumayte-eshche-raz-Sila-znaniya-o-neznanii.qEuXZQ.640589.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Grant_Podumayte-eshche-raz-Sila-znaniya-o-neznanii.qEuXZQ.640589.txt' 'Развитие/Grant_Podumayte-eshche-raz-Sila-znaniya-o-neznanii.qEuXZQ.640589.txt' && echo "MOVED: Grant_Podumayte-eshche-raz-Sila-znaniya-o-neznanii.qEuXZQ.640589.txt -> Развитие" >> "$LOG" || echo "FAIL: Grant_Podumayte-eshche-raz-Sila-znaniya-o-neznanii.qEuXZQ.640589.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Grant_Skrytyy-potencial-Nauka-dostizheniya-velikih-celey.VDBMtQ.819726.txt' ]; then
  echo "SKIP(exists): Grant_Skrytyy-potencial-Nauka-dostizheniya-velikih-celey.VDBMtQ.819726.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Grant_Skrytyy-potencial-Nauka-dostizheniya-velikih-celey.VDBMtQ.819726.txt' 'Развитие/Grant_Skrytyy-potencial-Nauka-dostizheniya-velikih-celey.VDBMtQ.819726.txt' && echo "MOVED: Grant_Skrytyy-potencial-Nauka-dostizheniya-velikih-celey.VDBMtQ.819726.txt -> Развитие" >> "$LOG" || echo "FAIL: Grant_Skrytyy-potencial-Nauka-dostizheniya-velikih-celey.VDBMtQ.819726.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Продажи/Grebenyuk_Otdel-prodazh-po-zahvatu-rynka.WeBxaA.542138.txt' ]; then
  echo "SKIP(exists): Grebenyuk_Otdel-prodazh-po-zahvatu-rynka.WeBxaA.542138.txt -> Продажи" >> "$LOG"
else
  mv 'свободные_книги/Grebenyuk_Otdel-prodazh-po-zahvatu-rynka.WeBxaA.542138.txt' 'Продажи/Grebenyuk_Otdel-prodazh-po-zahvatu-rynka.WeBxaA.542138.txt' && echo "MOVED: Grebenyuk_Otdel-prodazh-po-zahvatu-rynka.WeBxaA.542138.txt -> Продажи" >> "$LOG" || echo "FAIL: Grebenyuk_Otdel-prodazh-po-zahvatu-rynka.WeBxaA.542138.txt -> Продажи" >> "$LOG"
fi
if [ -e 'Развитие/Hardi_Budushchiy-ya-Kak-nachat-vypolnyat-dannye-sebe-obeshchaniya.OXNRhA.766789.txt' ]; then
  echo "SKIP(exists): Hardi_Budushchiy-ya-Kak-nachat-vypolnyat-dannye-sebe-obeshchaniya.OXNRhA.766789.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Hardi_Budushchiy-ya-Kak-nachat-vypolnyat-dannye-sebe-obeshchaniya.OXNRhA.766789.txt' 'Развитие/Hardi_Budushchiy-ya-Kak-nachat-vypolnyat-dannye-sebe-obeshchaniya.OXNRhA.766789.txt' && echo "MOVED: Hardi_Budushchiy-ya-Kak-nachat-vypolnyat-dannye-sebe-obeshchaniya.OXNRhA.766789.txt -> Развитие" >> "$LOG" || echo "FAIL: Hardi_Budushchiy-ya-Kak-nachat-vypolnyat-dannye-sebe-obeshchaniya.OXNRhA.766789.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Финансы/Harford_Ekonomist-pod-prikrytiem.sIrG6A.158903.fb2' ]; then
  echo "SKIP(exists): Harford_Ekonomist-pod-prikrytiem.sIrG6A.158903.fb2 -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Harford_Ekonomist-pod-prikrytiem.sIrG6A.158903.fb2' 'Финансы/Harford_Ekonomist-pod-prikrytiem.sIrG6A.158903.fb2' && echo "MOVED: Harford_Ekonomist-pod-prikrytiem.sIrG6A.158903.fb2 -> Финансы" >> "$LOG" || echo "FAIL: Harford_Ekonomist-pod-prikrytiem.sIrG6A.158903.fb2 -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/Harford_Ekonomist-pod-prikrytiem.sIrG6A.158903.txt' ]; then
  echo "SKIP(exists): Harford_Ekonomist-pod-prikrytiem.sIrG6A.158903.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Harford_Ekonomist-pod-prikrytiem.sIrG6A.158903.txt' 'Финансы/Harford_Ekonomist-pod-prikrytiem.sIrG6A.158903.txt' && echo "MOVED: Harford_Ekonomist-pod-prikrytiem.sIrG6A.158903.txt -> Финансы" >> "$LOG" || echo "FAIL: Harford_Ekonomist-pod-prikrytiem.sIrG6A.158903.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Тайм-менеджмент/Harford_Haos-Kak-besporyadok-menyaet-nashu-zhizn-k-luchshemu.y83I0A.506005.txt' ]; then
  echo "SKIP(exists): Harford_Haos-Kak-besporyadok-menyaet-nashu-zhizn-k-luchshemu.y83I0A.506005.txt -> Тайм-менеджмент" >> "$LOG"
else
  mv 'свободные_книги/Harford_Haos-Kak-besporyadok-menyaet-nashu-zhizn-k-luchshemu.y83I0A.506005.txt' 'Тайм-менеджмент/Harford_Haos-Kak-besporyadok-menyaet-nashu-zhizn-k-luchshemu.y83I0A.506005.txt' && echo "MOVED: Harford_Haos-Kak-besporyadok-menyaet-nashu-zhizn-k-luchshemu.y83I0A.506005.txt -> Тайм-менеджмент" >> "$LOG" || echo "FAIL: Harford_Haos-Kak-besporyadok-menyaet-nashu-zhizn-k-luchshemu.y83I0A.506005.txt -> Тайм-менеджмент" >> "$LOG"
fi
if [ -e 'Тайм-менеджмент/Hensson_Ne-shodite-s-uma-na-rabote.ftM1uA.552191.fb2' ]; then
  echo "SKIP(exists): Hensson_Ne-shodite-s-uma-na-rabote.ftM1uA.552191.fb2 -> Тайм-менеджмент" >> "$LOG"
else
  mv 'свободные_книги/Hensson_Ne-shodite-s-uma-na-rabote.ftM1uA.552191.fb2' 'Тайм-менеджмент/Hensson_Ne-shodite-s-uma-na-rabote.ftM1uA.552191.fb2' && echo "MOVED: Hensson_Ne-shodite-s-uma-na-rabote.ftM1uA.552191.fb2 -> Тайм-менеджмент" >> "$LOG" || echo "FAIL: Hensson_Ne-shodite-s-uma-na-rabote.ftM1uA.552191.fb2 -> Тайм-менеджмент" >> "$LOG"
fi
if [ -e 'Тайм-менеджмент/Hensson_Ne-shodite-s-uma-na-rabote.ftM1uA.552191.txt' ]; then
  echo "SKIP(exists): Hensson_Ne-shodite-s-uma-na-rabote.ftM1uA.552191.txt -> Тайм-менеджмент" >> "$LOG"
else
  mv 'свободные_книги/Hensson_Ne-shodite-s-uma-na-rabote.ftM1uA.552191.txt' 'Тайм-менеджмент/Hensson_Ne-shodite-s-uma-na-rabote.ftM1uA.552191.txt' && echo "MOVED: Hensson_Ne-shodite-s-uma-na-rabote.ftM1uA.552191.txt -> Тайм-менеджмент" >> "$LOG" || echo "FAIL: Hensson_Ne-shodite-s-uma-na-rabote.ftM1uA.552191.txt -> Тайм-менеджмент" >> "$LOG"
fi
if [ -e 'Общение, красноречие, голос/Kabeyn_Harizma-Kak-vliyat-ubezhdat-i-vdohnovlyat.GIdv4w.447216.txt' ]; then
  echo "SKIP(exists): Kabeyn_Harizma-Kak-vliyat-ubezhdat-i-vdohnovlyat.GIdv4w.447216.txt -> Общение, красноречие, голос" >> "$LOG"
else
  mv 'свободные_книги/Kabeyn_Harizma-Kak-vliyat-ubezhdat-i-vdohnovlyat.GIdv4w.447216.txt' 'Общение, красноречие, голос/Kabeyn_Harizma-Kak-vliyat-ubezhdat-i-vdohnovlyat.GIdv4w.447216.txt' && echo "MOVED: Kabeyn_Harizma-Kak-vliyat-ubezhdat-i-vdohnovlyat.GIdv4w.447216.txt -> Общение, красноречие, голос" >> "$LOG" || echo "FAIL: Kabeyn_Harizma-Kak-vliyat-ubezhdat-i-vdohnovlyat.GIdv4w.447216.txt -> Общение, красноречие, голос" >> "$LOG"
fi
if [ -e 'Развитие/Kasparov_Shahmaty-kak-model-zhizni.pj8KFg.105601.txt' ]; then
  echo "SKIP(exists): Kasparov_Shahmaty-kak-model-zhizni.pj8KFg.105601.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Kasparov_Shahmaty-kak-model-zhizni.pj8KFg.105601.txt' 'Развитие/Kasparov_Shahmaty-kak-model-zhizni.pj8KFg.105601.txt' && echo "MOVED: Kasparov_Shahmaty-kak-model-zhizni.pj8KFg.105601.txt -> Развитие" >> "$LOG" || echo "FAIL: Kasparov_Shahmaty-kak-model-zhizni.pj8KFg.105601.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Kemp_Snachala-skazhite-net-.xN23gA.284665.txt' ]; then
  echo "SKIP(exists): Kemp_Snachala-skazhite-net-.xN23gA.284665.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Kemp_Snachala-skazhite-net-.xN23gA.284665.txt' 'Развитие/Kemp_Snachala-skazhite-net-.xN23gA.284665.txt' && echo "MOVED: Kemp_Snachala-skazhite-net-.xN23gA.284665.txt -> Развитие" >> "$LOG" || echo "FAIL: Kemp_Snachala-skazhite-net-.xN23gA.284665.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Общение, красноречие, голос/Kennedi_Dogovoritsya-mozhno-obo-vsem-Kak-dobivatsya-maksimuma-v-lyubyh-peregovorah.pfRTSw.473148.txt' ]; then
  echo "SKIP(exists): Kennedi_Dogovoritsya-mozhno-obo-vsem-Kak-dobivatsya-maksimuma-v-lyubyh-peregovorah.pfRTSw.473148.txt -> Общение, красноречие, голос" >> "$LOG"
else
  mv 'свободные_книги/Kennedi_Dogovoritsya-mozhno-obo-vsem-Kak-dobivatsya-maksimuma-v-lyubyh-peregovorah.pfRTSw.473148.txt' 'Общение, красноречие, голос/Kennedi_Dogovoritsya-mozhno-obo-vsem-Kak-dobivatsya-maksimuma-v-lyubyh-peregovorah.pfRTSw.473148.txt' && echo "MOVED: Kennedi_Dogovoritsya-mozhno-obo-vsem-Kak-dobivatsya-maksimuma-v-lyubyh-peregovorah.pfRTSw.473148.txt -> Общение, красноречие, голос" >> "$LOG" || echo "FAIL: Kennedi_Dogovoritsya-mozhno-obo-vsem-Kak-dobivatsya-maksimuma-v-lyubyh-peregovorah.pfRTSw.473148.txt -> Общение, красноречие, голос" >> "$LOG"
fi
if [ -e 'Общение, красноречие, голос/Kerpen_Geniy-kommunikacii-Iskusstvo-prityagivat-lyudey-i-prevrashchat-ih-v-svoih-soyuznikov-11-navykov-effektivnogo-obshcheniya.06TRtA.569082.txt' ]; then
  echo "SKIP(exists): Kerpen_Geniy-kommunikacii-Iskusstvo-prityagivat-lyudey-i-prevrashchat-ih-v-svoih-soyuznikov-11-navykov-effektivnogo-obshcheniya.06TRtA.569082.txt -> Общение, красноречие, голос" >> "$LOG"
else
  mv 'свободные_книги/Kerpen_Geniy-kommunikacii-Iskusstvo-prityagivat-lyudey-i-prevrashchat-ih-v-svoih-soyuznikov-11-navykov-effektivnogo-obshcheniya.06TRtA.569082.txt' 'Общение, красноречие, голос/Kerpen_Geniy-kommunikacii-Iskusstvo-prityagivat-lyudey-i-prevrashchat-ih-v-svoih-soyuznikov-11-navykov-effektivnogo-obshcheniya.06TRtA.569082.txt' && echo "MOVED: Kerpen_Geniy-kommunikacii-Iskusstvo-prityagivat-lyudey-i-prevrashchat-ih-v-svoih-soyuznikov-11-navykov-effektivnogo-obshcheniya.06TRtA.569082.txt -> Общение, красноречие, голос" >> "$LOG" || echo "FAIL: Kerpen_Geniy-kommunikacii-Iskusstvo-prityagivat-lyudey-i-prevrashchat-ih-v-svoih-soyuznikov-11-navykov-effektivnogo-obshcheniya.06TRtA.569082.txt -> Общение, красноречие, голос" >> "$LOG"
fi
if [ -e 'Психология/Krzhnarik_Na-100-let-vpered-Iskusstvo-dolgosrochnogo-myshleniya-ili-Kak-chelovechestvo-razuchilos-du.txt' ]; then
  echo "SKIP(exists): Krzhnarik_Na-100-let-vpered-Iskusstvo-dolgosrochnogo-myshleniya-ili-Kak-chelovechestvo-razuchilos-du.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Krzhnarik_Na-100-let-vpered-Iskusstvo-dolgosrochnogo-myshleniya-ili-Kak-chelovechestvo-razuchilos-du.txt' 'Психология/Krzhnarik_Na-100-let-vpered-Iskusstvo-dolgosrochnogo-myshleniya-ili-Kak-chelovechestvo-razuchilos-du.txt' && echo "MOVED: Krzhnarik_Na-100-let-vpered-Iskusstvo-dolgosrochnogo-myshleniya-ili-Kak-chelovechestvo-razuchilos-du.txt -> Психология" >> "$LOG" || echo "FAIL: Krzhnarik_Na-100-let-vpered-Iskusstvo-dolgosrochnogo-myshleniya-ili-Kak-chelovechestvo-razuchilos-du.txt -> Психология" >> "$LOG"
fi
if [ -e 'Финансы/Lovenstayn_Kogda-geniy-terpit-porazhenie.I3QrMA.479775.txt' ]; then
  echo "SKIP(exists): Lovenstayn_Kogda-geniy-terpit-porazhenie.I3QrMA.479775.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Lovenstayn_Kogda-geniy-terpit-porazhenie.I3QrMA.479775.txt' 'Финансы/Lovenstayn_Kogda-geniy-terpit-porazhenie.I3QrMA.479775.txt' && echo "MOVED: Lovenstayn_Kogda-geniy-terpit-porazhenie.I3QrMA.479775.txt -> Финансы" >> "$LOG" || echo "FAIL: Lovenstayn_Kogda-geniy-terpit-porazhenie.I3QrMA.479775.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Развитие/Makgonigal_Sila-voli-Kak-razvit-i-ukrepit.R5j7IA.313552.txt' ]; then
  echo "SKIP(exists): Makgonigal_Sila-voli-Kak-razvit-i-ukrepit.R5j7IA.313552.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Makgonigal_Sila-voli-Kak-razvit-i-ukrepit.R5j7IA.313552.txt' 'Развитие/Makgonigal_Sila-voli-Kak-razvit-i-ukrepit.R5j7IA.313552.txt' && echo "MOVED: Makgonigal_Sila-voli-Kak-razvit-i-ukrepit.R5j7IA.313552.txt -> Развитие" >> "$LOG" || echo "FAIL: Makgonigal_Sila-voli-Kak-razvit-i-ukrepit.R5j7IA.313552.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Общение, красноречие, голос/Minto_Princip-piramidy-Minto.XfmJiw.525291.txt' ]; then
  echo "SKIP(exists): Minto_Princip-piramidy-Minto.XfmJiw.525291.txt -> Общение, красноречие, голос" >> "$LOG"
else
  mv 'свободные_книги/Minto_Princip-piramidy-Minto.XfmJiw.525291.txt' 'Общение, красноречие, голос/Minto_Princip-piramidy-Minto.XfmJiw.525291.txt' && echo "MOVED: Minto_Princip-piramidy-Minto.XfmJiw.525291.txt -> Общение, красноречие, голос" >> "$LOG" || echo "FAIL: Minto_Princip-piramidy-Minto.XfmJiw.525291.txt -> Общение, красноречие, голос" >> "$LOG"
fi
if [ -e 'Тайм-менеджмент/Moran_12-nedel-v-godu.ALzsAw.393326.fb2' ]; then
  echo "SKIP(exists): Moran_12-nedel-v-godu.ALzsAw.393326.fb2 -> Тайм-менеджмент" >> "$LOG"
else
  mv 'свободные_книги/Moran_12-nedel-v-godu.ALzsAw.393326.fb2' 'Тайм-менеджмент/Moran_12-nedel-v-godu.ALzsAw.393326.fb2' && echo "MOVED: Moran_12-nedel-v-godu.ALzsAw.393326.fb2 -> Тайм-менеджмент" >> "$LOG" || echo "FAIL: Moran_12-nedel-v-godu.ALzsAw.393326.fb2 -> Тайм-менеджмент" >> "$LOG"
fi
if [ -e 'Тайм-менеджмент/Moran_12-nedel-v-godu.ALzsAw.393326.txt' ]; then
  echo "SKIP(exists): Moran_12-nedel-v-godu.ALzsAw.393326.txt -> Тайм-менеджмент" >> "$LOG"
else
  mv 'свободные_книги/Moran_12-nedel-v-godu.ALzsAw.393326.txt' 'Тайм-менеджмент/Moran_12-nedel-v-godu.ALzsAw.393326.txt' && echo "MOVED: Moran_12-nedel-v-godu.ALzsAw.393326.txt -> Тайм-менеджмент" >> "$LOG" || echo "FAIL: Moran_12-nedel-v-godu.ALzsAw.393326.txt -> Тайм-менеджмент" >> "$LOG"
fi
if [ -e 'Эзотерика, духовность/Paskal_Mysli.UlEVMw.584327.fb2' ]; then
  echo "SKIP(exists): Paskal_Mysli.UlEVMw.584327.fb2 -> Эзотерика, духовность" >> "$LOG"
else
  mv 'свободные_книги/Paskal_Mysli.UlEVMw.584327.fb2' 'Эзотерика, духовность/Paskal_Mysli.UlEVMw.584327.fb2' && echo "MOVED: Paskal_Mysli.UlEVMw.584327.fb2 -> Эзотерика, духовность" >> "$LOG" || echo "FAIL: Paskal_Mysli.UlEVMw.584327.fb2 -> Эзотерика, духовность" >> "$LOG"
fi
if [ -e 'Продажи/Piling_Iskusstvo-peregovorov-Chto-luchshie-peregovorshchiki-znayut-delayut-i-govoryat.I2YvRg.458656.fb2' ]; then
  echo "SKIP(exists): Piling_Iskusstvo-peregovorov-Chto-luchshie-peregovorshchiki-znayut-delayut-i-govoryat.I2YvRg.458656.fb2 -> Продажи" >> "$LOG"
else
  mv 'свободные_книги/Piling_Iskusstvo-peregovorov-Chto-luchshie-peregovorshchiki-znayut-delayut-i-govoryat.I2YvRg.458656.fb2' 'Продажи/Piling_Iskusstvo-peregovorov-Chto-luchshie-peregovorshchiki-znayut-delayut-i-govoryat.I2YvRg.458656.fb2' && echo "MOVED: Piling_Iskusstvo-peregovorov-Chto-luchshie-peregovorshchiki-znayut-delayut-i-govoryat.I2YvRg.458656.fb2 -> Продажи" >> "$LOG" || echo "FAIL: Piling_Iskusstvo-peregovorov-Chto-luchshie-peregovorshchiki-znayut-delayut-i-govoryat.I2YvRg.458656.fb2 -> Продажи" >> "$LOG"
fi
if [ -e 'Продажи/Piling_Iskusstvo-peregovorov-Chto-luchshie-peregovorshchiki-znayut-delayut-i-govoryat.I2YvRg.458656.txt' ]; then
  echo "SKIP(exists): Piling_Iskusstvo-peregovorov-Chto-luchshie-peregovorshchiki-znayut-delayut-i-govoryat.I2YvRg.458656.txt -> Продажи" >> "$LOG"
else
  mv 'свободные_книги/Piling_Iskusstvo-peregovorov-Chto-luchshie-peregovorshchiki-znayut-delayut-i-govoryat.I2YvRg.458656.txt' 'Продажи/Piling_Iskusstvo-peregovorov-Chto-luchshie-peregovorshchiki-znayut-delayut-i-govoryat.I2YvRg.458656.txt' && echo "MOVED: Piling_Iskusstvo-peregovorov-Chto-luchshie-peregovorshchiki-znayut-delayut-i-govoryat.I2YvRg.458656.txt -> Продажи" >> "$LOG" || echo "FAIL: Piling_Iskusstvo-peregovorov-Chto-luchshie-peregovorshchiki-znayut-delayut-i-govoryat.I2YvRg.458656.txt -> Продажи" >> "$LOG"
fi
if [ -e 'Продажи/Pink_Cheloveku-svoystvenno-prodavat-Udivitelnaya-pravda-o-tom-kak-pobuzhdat-drugih-k-deystviyu.c_TDCQ.425795.fb2' ]; then
  echo "SKIP(exists): Pink_Cheloveku-svoystvenno-prodavat-Udivitelnaya-pravda-o-tom-kak-pobuzhdat-drugih-k-deystviyu.c_TDCQ.425795.fb2 -> Продажи" >> "$LOG"
else
  mv 'свободные_книги/Pink_Cheloveku-svoystvenno-prodavat-Udivitelnaya-pravda-o-tom-kak-pobuzhdat-drugih-k-deystviyu.c_TDCQ.425795.fb2' 'Продажи/Pink_Cheloveku-svoystvenno-prodavat-Udivitelnaya-pravda-o-tom-kak-pobuzhdat-drugih-k-deystviyu.c_TDCQ.425795.fb2' && echo "MOVED: Pink_Cheloveku-svoystvenno-prodavat-Udivitelnaya-pravda-o-tom-kak-pobuzhdat-drugih-k-deystviyu.c_TDCQ.425795.fb2 -> Продажи" >> "$LOG" || echo "FAIL: Pink_Cheloveku-svoystvenno-prodavat-Udivitelnaya-pravda-o-tom-kak-pobuzhdat-drugih-k-deystviyu.c_TDCQ.425795.fb2 -> Продажи" >> "$LOG"
fi
if [ -e 'Общение, красноречие, голос/Pozharskaya_Rechevaya-samooborona.Z5XGnA.482317.txt' ]; then
  echo "SKIP(exists): Pozharskaya_Rechevaya-samooborona.Z5XGnA.482317.txt -> Общение, красноречие, голос" >> "$LOG"
else
  mv 'свободные_книги/Pozharskaya_Rechevaya-samooborona.Z5XGnA.482317.txt' 'Общение, красноречие, голос/Pozharskaya_Rechevaya-samooborona.Z5XGnA.482317.txt' && echo "MOVED: Pozharskaya_Rechevaya-samooborona.Z5XGnA.482317.txt -> Общение, красноречие, голос" >> "$LOG" || echo "FAIL: Pozharskaya_Rechevaya-samooborona.Z5XGnA.482317.txt -> Общение, красноречие, голос" >> "$LOG"
fi
if [ -e 'Продажи/Rekhem_SPIN-prodazhi.4j4ftQ.313102.txt' ]; then
  echo "SKIP(exists): Rekhem_SPIN-prodazhi.4j4ftQ.313102.txt -> Продажи" >> "$LOG"
else
  mv 'свободные_книги/Rekhem_SPIN-prodazhi.4j4ftQ.313102.txt' 'Продажи/Rekhem_SPIN-prodazhi.4j4ftQ.313102.txt' && echo "MOVED: Rekhem_SPIN-prodazhi.4j4ftQ.313102.txt -> Продажи" >> "$LOG" || echo "FAIL: Rekhem_SPIN-prodazhi.4j4ftQ.313102.txt -> Продажи" >> "$LOG"
fi
if [ -e 'Общение, красноречие, голос/Sheynov_Govorit-net-ne-ispytyvaya-chuvstva-viny.7ML88g.385417.txt' ]; then
  echo "SKIP(exists): Sheynov_Govorit-net-ne-ispytyvaya-chuvstva-viny.7ML88g.385417.txt -> Общение, красноречие, голос" >> "$LOG"
else
  mv 'свободные_книги/Sheynov_Govorit-net-ne-ispytyvaya-chuvstva-viny.7ML88g.385417.txt' 'Общение, красноречие, голос/Sheynov_Govorit-net-ne-ispytyvaya-chuvstva-viny.7ML88g.385417.txt' && echo "MOVED: Sheynov_Govorit-net-ne-ispytyvaya-chuvstva-viny.7ML88g.385417.txt -> Общение, красноречие, голос" >> "$LOG" || echo "FAIL: Sheynov_Govorit-net-ne-ispytyvaya-chuvstva-viny.7ML88g.385417.txt -> Общение, красноречие, голос" >> "$LOG"
fi
if [ -e 'Развитие/Shtayner_Filosofiya-svobody-Osnovnye-cherty-odnogo-sovremennogo-mirovozzreniya.4jLtQQ.843606.txt' ]; then
  echo "SKIP(exists): Shtayner_Filosofiya-svobody-Osnovnye-cherty-odnogo-sovremennogo-mirovozzreniya.4jLtQQ.843606.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Shtayner_Filosofiya-svobody-Osnovnye-cherty-odnogo-sovremennogo-mirovozzreniya.4jLtQQ.843606.txt' 'Развитие/Shtayner_Filosofiya-svobody-Osnovnye-cherty-odnogo-sovremennogo-mirovozzreniya.4jLtQQ.843606.txt' && echo "MOVED: Shtayner_Filosofiya-svobody-Osnovnye-cherty-odnogo-sovremennogo-mirovozzreniya.4jLtQQ.843606.txt -> Развитие" >> "$LOG" || echo "FAIL: Shtayner_Filosofiya-svobody-Osnovnye-cherty-odnogo-sovremennogo-mirovozzreniya.4jLtQQ.843606.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Продажи/Snayder_K-chertu-ceny-Sozdavayte-cennost-SPIN-prodazhi-v-novyh-usloviyah.TogI1w.269593.txt' ]; then
  echo "SKIP(exists): Snayder_K-chertu-ceny-Sozdavayte-cennost-SPIN-prodazhi-v-novyh-usloviyah.TogI1w.269593.txt -> Продажи" >> "$LOG"
else
  mv 'свободные_книги/Snayder_K-chertu-ceny-Sozdavayte-cennost-SPIN-prodazhi-v-novyh-usloviyah.TogI1w.269593.txt' 'Продажи/Snayder_K-chertu-ceny-Sozdavayte-cennost-SPIN-prodazhi-v-novyh-usloviyah.TogI1w.269593.txt' && echo "MOVED: Snayder_K-chertu-ceny-Sozdavayte-cennost-SPIN-prodazhi-v-novyh-usloviyah.TogI1w.269593.txt -> Продажи" >> "$LOG" || echo "FAIL: Snayder_K-chertu-ceny-Sozdavayte-cennost-SPIN-prodazhi-v-novyh-usloviyah.TogI1w.269593.txt -> Продажи" >> "$LOG"
fi
if [ -e 'Развитие/Transcend.txt' ]; then
  echo "SKIP(exists): Transcend.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Transcend.txt' 'Развитие/Transcend.txt' && echo "MOVED: Transcend.txt -> Развитие" >> "$LOG" || echo "FAIL: Transcend.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Transcend2..txt' ]; then
  echo "SKIP(exists): Transcend2..txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Transcend2..txt' 'Развитие/Transcend2..txt' && echo "MOVED: Transcend2..txt -> Развитие" >> "$LOG" || echo "FAIL: Transcend2..txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Treysi_Vyydi-iz-zony-komforta-Izmeni-svoyu-zhizn.t4MEIg.342476.txt' ]; then
  echo "SKIP(exists): Treysi_Vyydi-iz-zony-komforta-Izmeni-svoyu-zhizn.t4MEIg.342476.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Treysi_Vyydi-iz-zony-komforta-Izmeni-svoyu-zhizn.t4MEIg.342476.txt' 'Развитие/Treysi_Vyydi-iz-zony-komforta-Izmeni-svoyu-zhizn.t4MEIg.342476.txt' && echo "MOVED: Treysi_Vyydi-iz-zony-komforta-Izmeni-svoyu-zhizn.t4MEIg.342476.txt -> Развитие" >> "$LOG" || echo "FAIL: Treysi_Vyydi-iz-zony-komforta-Izmeni-svoyu-zhizn.t4MEIg.342476.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Продажи/Yuri_Peregovory-bez-porazheniya-Garvardskiy-metod.c3U1wg.507992.txt' ]; then
  echo "SKIP(exists): Yuri_Peregovory-bez-porazheniya-Garvardskiy-metod.c3U1wg.507992.txt -> Продажи" >> "$LOG"
else
  mv 'свободные_книги/Yuri_Peregovory-bez-porazheniya-Garvardskiy-metod.c3U1wg.507992.txt' 'Продажи/Yuri_Peregovory-bez-porazheniya-Garvardskiy-metod.c3U1wg.507992.txt' && echo "MOVED: Yuri_Peregovory-bez-porazheniya-Garvardskiy-metod.c3U1wg.507992.txt -> Продажи" >> "$LOG" || echo "FAIL: Yuri_Peregovory-bez-porazheniya-Garvardskiy-metod.c3U1wg.507992.txt -> Продажи" >> "$LOG"
fi
if [ -e 'Продажи/Ziglar_Sekrety-zaklyucheniya-sdelok.gkuIJQ.427828.fb2' ]; then
  echo "SKIP(exists): Ziglar_Sekrety-zaklyucheniya-sdelok.gkuIJQ.427828.fb2 -> Продажи" >> "$LOG"
else
  mv 'свободные_книги/Ziglar_Sekrety-zaklyucheniya-sdelok.gkuIJQ.427828.fb2' 'Продажи/Ziglar_Sekrety-zaklyucheniya-sdelok.gkuIJQ.427828.fb2' && echo "MOVED: Ziglar_Sekrety-zaklyucheniya-sdelok.gkuIJQ.427828.fb2 -> Продажи" >> "$LOG" || echo "FAIL: Ziglar_Sekrety-zaklyucheniya-sdelok.gkuIJQ.427828.fb2 -> Продажи" >> "$LOG"
fi
if [ -e 'Продажи/Ziglar_Sekrety-zaklyucheniya-sdelok.gkuIJQ.427828.txt' ]; then
  echo "SKIP(exists): Ziglar_Sekrety-zaklyucheniya-sdelok.gkuIJQ.427828.txt -> Продажи" >> "$LOG"
else
  mv 'свободные_книги/Ziglar_Sekrety-zaklyucheniya-sdelok.gkuIJQ.427828.txt' 'Продажи/Ziglar_Sekrety-zaklyucheniya-sdelok.gkuIJQ.427828.txt' && echo "MOVED: Ziglar_Sekrety-zaklyucheniya-sdelok.gkuIJQ.427828.txt -> Продажи" >> "$LOG" || echo "FAIL: Ziglar_Sekrety-zaklyucheniya-sdelok.gkuIJQ.427828.txt -> Продажи" >> "$LOG"
fi
if [ -e 'Развитие/[Не]правда о нашем теле.txt' ]; then
  echo "SKIP(exists): [Не]правда о нашем теле.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/[Не]правда о нашем теле.txt' 'Развитие/[Не]правда о нашем теле.txt' && echo "MOVED: [Не]правда о нашем теле.txt -> Развитие" >> "$LOG" || echo "FAIL: [Не]правда о нашем теле.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Продажи/barysheva-kak-prodat.txt' ]; then
  echo "SKIP(exists): barysheva-kak-prodat.txt -> Продажи" >> "$LOG"
else
  mv 'свободные_книги/barysheva-kak-prodat.txt' 'Продажи/barysheva-kak-prodat.txt' && echo "MOVED: barysheva-kak-prodat.txt -> Продажи" >> "$LOG" || echo "FAIL: barysheva-kak-prodat.txt -> Продажи" >> "$LOG"
fi
if [ -e 'Продажи/nil_rekhem-spin-prodazhi-61f236343023e.fb2.zip' ]; then
  echo "SKIP(exists): nil_rekhem-spin-prodazhi-61f236343023e.fb2.zip -> Продажи" >> "$LOG"
else
  mv 'свободные_книги/nil_rekhem-spin-prodazhi-61f236343023e.fb2.zip' 'Продажи/nil_rekhem-spin-prodazhi-61f236343023e.fb2.zip' && echo "MOVED: nil_rekhem-spin-prodazhi-61f236343023e.fb2.zip -> Продажи" >> "$LOG" || echo "FAIL: nil_rekhem-spin-prodazhi-61f236343023e.fb2.zip -> Продажи" >> "$LOG"
fi
if [ -e 'Финансы/obuchenie-finansovoy-gramotnosti.-prostye-recepty-povysheniya-blagosostoyaniya.txt' ]; then
  echo "SKIP(exists): obuchenie-finansovoy-gramotnosti.-prostye-recepty-povysheniya-blagosostoyaniya.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/obuchenie-finansovoy-gramotnosti.-prostye-recepty-povysheniya-blagosostoyaniya.txt' 'Финансы/obuchenie-finansovoy-gramotnosti.-prostye-recepty-povysheniya-blagosostoyaniya.txt' && echo "MOVED: obuchenie-finansovoy-gramotnosti.-prostye-recepty-povysheniya-blagosostoyaniya.txt -> Финансы" >> "$LOG" || echo "FAIL: obuchenie-finansovoy-gramotnosti.-prostye-recepty-povysheniya-blagosostoyaniya.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Эзотерика, духовность/paskal-mysli-ulevmw.txt' ]; then
  echo "SKIP(exists): paskal-mysli-ulevmw.txt -> Эзотерика, духовность" >> "$LOG"
else
  mv 'свободные_книги/paskal-mysli-ulevmw.txt' 'Эзотерика, духовность/paskal-mysli-ulevmw.txt' && echo "MOVED: paskal-mysli-ulevmw.txt -> Эзотерика, духовность" >> "$LOG" || echo "FAIL: paskal-mysli-ulevmw.txt -> Эзотерика, духовность" >> "$LOG"
fi
if [ -e 'Развитие/Азбука системного мышлени.txt' ]; then
  echo "SKIP(exists): Азбука системного мышлени.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Азбука системного мышлени.txt' 'Развитие/Азбука системного мышлени.txt' && echo "MOVED: Азбука системного мышлени.txt -> Развитие" >> "$LOG" || echo "FAIL: Азбука системного мышлени.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Атомные привычки. Как приобрести хорошие привычки и избавиться от плохих.txt' ]; then
  echo "SKIP(exists): Атомные привычки. Как приобрести хорошие привычки и избавиться от плохих.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Атомные привычки. Как приобрести хорошие привычки и избавиться от плохих.txt' 'Развитие/Атомные привычки. Как приобрести хорошие привычки и избавиться от плохих.txt' && echo "MOVED: Атомные привычки. Как приобрести хорошие привычки и избавиться от плохих.txt -> Развитие" >> "$LOG" || echo "FAIL: Атомные привычки. Как приобрести хорошие привычки и избавиться от плохих.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Психология/Беспокойный ум. Моя победа над биполярным расстройством.txt' ]; then
  echo "SKIP(exists): Беспокойный ум. Моя победа над биполярным расстройством.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Беспокойный ум. Моя победа над биполярным расстройством.txt' 'Психология/Беспокойный ум. Моя победа над биполярным расстройством.txt' && echo "MOVED: Беспокойный ум. Моя победа над биполярным расстройством.txt -> Психология" >> "$LOG" || echo "FAIL: Беспокойный ум. Моя победа над биполярным расстройством.txt -> Психология" >> "$LOG"
fi
if [ -e 'Финансы/Боги_денег_(Часть_1).txt' ]; then
  echo "SKIP(exists): Боги_денег_(Часть_1).txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Боги_денег_(Часть_1).txt' 'Финансы/Боги_денег_(Часть_1).txt' && echo "MOVED: Боги_денег_(Часть_1).txt -> Финансы" >> "$LOG" || echo "FAIL: Боги_денег_(Часть_1).txt -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/Боги_денег_(Часть_2).txt' ]; then
  echo "SKIP(exists): Боги_денег_(Часть_2).txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Боги_денег_(Часть_2).txt' 'Финансы/Боги_денег_(Часть_2).txt' && echo "MOVED: Боги_денег_(Часть_2).txt -> Финансы" >> "$LOG" || echo "FAIL: Боги_денег_(Часть_2).txt -> Финансы" >> "$LOG"
fi
if [ -e 'Психология/Быть собой. Новая теория сознания - часть 1.txt' ]; then
  echo "SKIP(exists): Быть собой. Новая теория сознания - часть 1.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Быть собой. Новая теория сознания - часть 1.txt' 'Психология/Быть собой. Новая теория сознания - часть 1.txt' && echo "MOVED: Быть собой. Новая теория сознания - часть 1.txt -> Психология" >> "$LOG" || echo "FAIL: Быть собой. Новая теория сознания - часть 1.txt -> Психология" >> "$LOG"
fi
if [ -e 'Психология/Быть собой. Новая теория сознания - часть 2.txt' ]; then
  echo "SKIP(exists): Быть собой. Новая теория сознания - часть 2.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Быть собой. Новая теория сознания - часть 2.txt' 'Психология/Быть собой. Новая теория сознания - часть 2.txt' && echo "MOVED: Быть собой. Новая теория сознания - часть 2.txt -> Психология" >> "$LOG" || echo "FAIL: Быть собой. Новая теория сознания - часть 2.txt -> Психология" >> "$LOG"
fi
if [ -e 'Общение, красноречие, голос/В_начале_было_Слово,_а_в_конце_будет_цифра.txt' ]; then
  echo "SKIP(exists): В_начале_было_Слово,_а_в_конце_будет_цифра.txt -> Общение, красноречие, голос" >> "$LOG"
else
  mv 'свободные_книги/В_начале_было_Слово,_а_в_конце_будет_цифра.txt' 'Общение, красноречие, голос/В_начале_было_Слово,_а_в_конце_будет_цифра.txt' && echo "MOVED: В_начале_было_Слово,_а_в_конце_будет_цифра.txt -> Общение, красноречие, голос" >> "$LOG" || echo "FAIL: В_начале_было_Слово,_а_в_конце_будет_цифра.txt -> Общение, красноречие, голос" >> "$LOG"
fi
if [ -e 'Общение, красноречие, голос/В_начале_было_Слово,_а_в_конце_будет_цифра2.txt' ]; then
  echo "SKIP(exists): В_начале_было_Слово,_а_в_конце_будет_цифра2.txt -> Общение, красноречие, голос" >> "$LOG"
else
  mv 'свободные_книги/В_начале_было_Слово,_а_в_конце_будет_цифра2.txt' 'Общение, красноречие, голос/В_начале_было_Слово,_а_в_конце_будет_цифра2.txt' && echo "MOVED: В_начале_было_Слово,_а_в_конце_будет_цифра2.txt -> Общение, красноречие, голос" >> "$LOG" || echo "FAIL: В_начале_было_Слово,_а_в_конце_будет_цифра2.txt -> Общение, красноречие, голос" >> "$LOG"
fi
if [ -e 'Общение, красноречие, голос/В_начале_было_Слово,_а_в_конце_будет_цифра3.txt' ]; then
  echo "SKIP(exists): В_начале_было_Слово,_а_в_конце_будет_цифра3.txt -> Общение, красноречие, голос" >> "$LOG"
else
  mv 'свободные_книги/В_начале_было_Слово,_а_в_конце_будет_цифра3.txt' 'Общение, красноречие, голос/В_начале_было_Слово,_а_в_конце_будет_цифра3.txt' && echo "MOVED: В_начале_было_Слово,_а_в_конце_будет_цифра3.txt -> Общение, красноречие, голос" >> "$LOG" || echo "FAIL: В_начале_было_Слово,_а_в_конце_будет_цифра3.txt -> Общение, красноречие, голос" >> "$LOG"
fi
if [ -e 'Развитие/Величайший блеф. Как я научилась быть внимательной, владеть собой и побеждать - часть 1.txt' ]; then
  echo "SKIP(exists): Величайший блеф. Как я научилась быть внимательной, владеть собой и побеждать - часть 1.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Величайший блеф. Как я научилась быть внимательной, владеть собой и побеждать - часть 1.txt' 'Развитие/Величайший блеф. Как я научилась быть внимательной, владеть собой и побеждать - часть 1.txt' && echo "MOVED: Величайший блеф. Как я научилась быть внимательной, владеть собой и побеждать - часть 1.txt -> Развитие" >> "$LOG" || echo "FAIL: Величайший блеф. Как я научилась быть внимательной, владеть собой и побеждать - часть 1.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Величайший блеф. Как я научилась быть внимательной, владеть собой и побеждать - часть 2.txt' ]; then
  echo "SKIP(exists): Величайший блеф. Как я научилась быть внимательной, владеть собой и побеждать - часть 2.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Величайший блеф. Как я научилась быть внимательной, владеть собой и побеждать - часть 2.txt' 'Развитие/Величайший блеф. Как я научилась быть внимательной, владеть собой и побеждать - часть 2.txt' && echo "MOVED: Величайший блеф. Как я научилась быть внимательной, владеть собой и побеждать - часть 2.txt -> Развитие" >> "$LOG" || echo "FAIL: Величайший блеф. Как я научилась быть внимательной, владеть собой и побеждать - часть 2.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Общение, красноречие, голос/Власть_голоса.txt' ]; then
  echo "SKIP(exists): Власть_голоса.txt -> Общение, красноречие, голос" >> "$LOG"
else
  mv 'свободные_книги/Власть_голоса.txt' 'Общение, красноречие, голос/Власть_голоса.txt' && echo "MOVED: Власть_голоса.txt -> Общение, красноречие, голос" >> "$LOG" || echo "FAIL: Власть_голоса.txt -> Общение, красноречие, голос" >> "$LOG"
fi
if [ -e 'Развитие/Внутренний опыт.txt' ]; then
  echo "SKIP(exists): Внутренний опыт.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Внутренний опыт.txt' 'Развитие/Внутренний опыт.txt' && echo "MOVED: Внутренний опыт.txt -> Развитие" >> "$LOG" || echo "FAIL: Внутренний опыт.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Психология/Воля и самоконтроль.txt' ]; then
  echo "SKIP(exists): Воля и самоконтроль.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Воля и самоконтроль.txt' 'Психология/Воля и самоконтроль.txt' && echo "MOVED: Воля и самоконтроль.txt -> Психология" >> "$LOG" || echo "FAIL: Воля и самоконтроль.txt -> Психология" >> "$LOG"
fi
if [ -e 'Психология/Воля_и_самоконтроль2.txt' ]; then
  echo "SKIP(exists): Воля_и_самоконтроль2.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Воля_и_самоконтроль2.txt' 'Психология/Воля_и_самоконтроль2.txt' && echo "MOVED: Воля_и_самоконтроль2.txt -> Психология" >> "$LOG" || echo "FAIL: Воля_и_самоконтроль2.txt -> Психология" >> "$LOG"
fi
if [ -e 'Финансы/Восхождение денег.txt' ]; then
  echo "SKIP(exists): Восхождение денег.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Восхождение денег.txt' 'Финансы/Восхождение денег.txt' && echo "MOVED: Восхождение денег.txt -> Финансы" >> "$LOG" || echo "FAIL: Восхождение денег.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/Восхождение_денег.txt' ]; then
  echo "SKIP(exists): Восхождение_денег.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Восхождение_денег.txt' 'Финансы/Восхождение_денег.txt' && echo "MOVED: Восхождение_денег.txt -> Финансы" >> "$LOG" || echo "FAIL: Восхождение_денег.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/Восхождение_денегч2.txt' ]; then
  echo "SKIP(exists): Восхождение_денегч2.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Восхождение_денегч2.txt' 'Финансы/Восхождение_денегч2.txt' && echo "MOVED: Восхождение_денегч2.txt -> Финансы" >> "$LOG" || echo "FAIL: Восхождение_денегч2.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Развитие/Восьмой навык. От эффективности к величию - часть 1.txt' ]; then
  echo "SKIP(exists): Восьмой навык. От эффективности к величию - часть 1.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Восьмой навык. От эффективности к величию - часть 1.txt' 'Развитие/Восьмой навык. От эффективности к величию - часть 1.txt' && echo "MOVED: Восьмой навык. От эффективности к величию - часть 1.txt -> Развитие" >> "$LOG" || echo "FAIL: Восьмой навык. От эффективности к величию - часть 1.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Восьмой навык. От эффективности к величию - часть 2.txt' ]; then
  echo "SKIP(exists): Восьмой навык. От эффективности к величию - часть 2.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Восьмой навык. От эффективности к величию - часть 2.txt' 'Развитие/Восьмой навык. От эффективности к величию - часть 2.txt' && echo "MOVED: Восьмой навык. От эффективности к величию - часть 2.txt -> Развитие" >> "$LOG" || echo "FAIL: Восьмой навык. От эффективности к величию - часть 2.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Голая_статистика ч1.txt' ]; then
  echo "SKIP(exists): Голая_статистика ч1.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Голая_статистика ч1.txt' 'Развитие/Голая_статистика ч1.txt' && echo "MOVED: Голая_статистика ч1.txt -> Развитие" >> "$LOG" || echo "FAIL: Голая_статистика ч1.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Голая_статистика ч2.txt' ]; then
  echo "SKIP(exists): Голая_статистика ч2.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Голая_статистика ч2.txt' 'Развитие/Голая_статистика ч2.txt' && echo "MOVED: Голая_статистика ч2.txt -> Развитие" >> "$LOG" || echo "FAIL: Голая_статистика ч2.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Голая_статистика.txt' ]; then
  echo "SKIP(exists): Голая_статистика.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Голая_статистика.txt' 'Развитие/Голая_статистика.txt' && echo "MOVED: Голая_статистика.txt -> Развитие" >> "$LOG" || echo "FAIL: Голая_статистика.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Головоломки и развлечения_transcription.txt' ]; then
  echo "SKIP(exists): Головоломки и развлечения_transcription.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Головоломки и развлечения_transcription.txt' 'Развитие/Головоломки и развлечения_transcription.txt' && echo "MOVED: Головоломки и развлечения_transcription.txt -> Развитие" >> "$LOG" || echo "FAIL: Головоломки и развлечения_transcription.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Головоломки. Задачи. Фокусы. Развлечения_transcription.txt' ]; then
  echo "SKIP(exists): Головоломки. Задачи. Фокусы. Развлечения_transcription.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Головоломки. Задачи. Фокусы. Развлечения_transcription.txt' 'Развитие/Головоломки. Задачи. Фокусы. Развлечения_transcription.txt' && echo "MOVED: Головоломки. Задачи. Фокусы. Развлечения_transcription.txt -> Развитие" >> "$LOG" || echo "FAIL: Головоломки. Задачи. Фокусы. Развлечения_transcription.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Финансы/ДУмай как миллионер.txt' ]; then
  echo "SKIP(exists): ДУмай как миллионер.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/ДУмай как миллионер.txt' 'Финансы/ДУмай как миллионер.txt' && echo "MOVED: ДУмай как миллионер.txt -> Финансы" >> "$LOG" || echo "FAIL: ДУмай как миллионер.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/Деньги. Мастер игры1.txt' ]; then
  echo "SKIP(exists): Деньги. Мастер игры1.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Деньги. Мастер игры1.txt' 'Финансы/Деньги. Мастер игры1.txt' && echo "MOVED: Деньги. Мастер игры1.txt -> Финансы" >> "$LOG" || echo "FAIL: Деньги. Мастер игры1.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/Деньги. Мастер игры2.txt' ]; then
  echo "SKIP(exists): Деньги. Мастер игры2.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Деньги. Мастер игры2.txt' 'Финансы/Деньги. Мастер игры2.txt' && echo "MOVED: Деньги. Мастер игры2.txt -> Финансы" >> "$LOG" || echo "FAIL: Деньги. Мастер игры2.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/Деньги. Мастер игры3.txt' ]; then
  echo "SKIP(exists): Деньги. Мастер игры3.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Деньги. Мастер игры3.txt' 'Финансы/Деньги. Мастер игры3.txt' && echo "MOVED: Деньги. Мастер игры3.txt -> Финансы" >> "$LOG" || echo "FAIL: Деньги. Мастер игры3.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Здоровье/Диета для ускорения метаболизма.txt' ]; then
  echo "SKIP(exists): Диета для ускорения метаболизма.txt -> Здоровье" >> "$LOG"
else
  mv 'свободные_книги/Диета для ускорения метаболизма.txt' 'Здоровье/Диета для ускорения метаболизма.txt' && echo "MOVED: Диета для ускорения метаболизма.txt -> Здоровье" >> "$LOG" || echo "FAIL: Диета для ускорения метаболизма.txt -> Здоровье" >> "$LOG"
fi
if [ -e 'Развитие/Дофамин самый нужный гормон.txt' ]; then
  echo "SKIP(exists): Дофамин самый нужный гормон.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Дофамин самый нужный гормон.txt' 'Развитие/Дофамин самый нужный гормон.txt' && echo "MOVED: Дофамин самый нужный гормон.txt -> Развитие" >> "$LOG" || echo "FAIL: Дофамин самый нужный гормон.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Финансы/Душа денег.txt' ]; then
  echo "SKIP(exists): Душа денег.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Душа денег.txt' 'Финансы/Душа денег.txt' && echo "MOVED: Душа денег.txt -> Финансы" >> "$LOG" || echo "FAIL: Душа денег.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Здоровье/Еда. Отправная точка. Какими мы станем в будущем, если не изменим себя в настоящем - часть 1.txt' ]; then
  echo "SKIP(exists): Еда. Отправная точка. Какими мы станем в будущем, если не изменим себя в настоящем - часть 1.txt -> Здоровье" >> "$LOG"
else
  mv 'свободные_книги/Еда. Отправная точка. Какими мы станем в будущем, если не изменим себя в настоящем - часть 1.txt' 'Здоровье/Еда. Отправная точка. Какими мы станем в будущем, если не изменим себя в настоящем - часть 1.txt' && echo "MOVED: Еда. Отправная точка. Какими мы станем в будущем, если не изменим себя в настоящем - часть 1.txt -> Здоровье" >> "$LOG" || echo "FAIL: Еда. Отправная точка. Какими мы станем в будущем, если не изменим себя в настоящем - часть 1.txt -> Здоровье" >> "$LOG"
fi
if [ -e 'Здоровье/Еда. Отправная точка. Какими мы станем в будущем, если не изменим себя в настоящем - часть 2.txt' ]; then
  echo "SKIP(exists): Еда. Отправная точка. Какими мы станем в будущем, если не изменим себя в настоящем - часть 2.txt -> Здоровье" >> "$LOG"
else
  mv 'свободные_книги/Еда. Отправная точка. Какими мы станем в будущем, если не изменим себя в настоящем - часть 2.txt' 'Здоровье/Еда. Отправная точка. Какими мы станем в будущем, если не изменим себя в настоящем - часть 2.txt' && echo "MOVED: Еда. Отправная точка. Какими мы станем в будущем, если не изменим себя в настоящем - часть 2.txt -> Здоровье" >> "$LOG" || echo "FAIL: Еда. Отправная точка. Какими мы станем в будущем, если не изменим себя в настоящем - часть 2.txt -> Здоровье" >> "$LOG"
fi
if [ -e 'Здоровье/Еда.Отправная точка..txt' ]; then
  echo "SKIP(exists): Еда.Отправная точка..txt -> Здоровье" >> "$LOG"
else
  mv 'свободные_книги/Еда.Отправная точка..txt' 'Здоровье/Еда.Отправная точка..txt' && echo "MOVED: Еда.Отправная точка..txt -> Здоровье" >> "$LOG" || echo "FAIL: Еда.Отправная точка..txt -> Здоровье" >> "$LOG"
fi
if [ -e 'Бизнес, менеджмент/Жесткий менеджмент. Заставьте людей работать на.txt' ]; then
  echo "SKIP(exists): Жесткий менеджмент. Заставьте людей работать на.txt -> Бизнес, менеджмент" >> "$LOG"
else
  mv 'свободные_книги/Жесткий менеджмент. Заставьте людей работать на.txt' 'Бизнес, менеджмент/Жесткий менеджмент. Заставьте людей работать на.txt' && echo "MOVED: Жесткий менеджмент. Заставьте людей работать на.txt -> Бизнес, менеджмент" >> "$LOG" || echo "FAIL: Жесткий менеджмент. Заставьте людей работать на.txt -> Бизнес, менеджмент" >> "$LOG"
fi
if [ -e 'Психология/Живи с чувством. Как поставить цели, к которым лежит душа.txt' ]; then
  echo "SKIP(exists): Живи с чувством. Как поставить цели, к которым лежит душа.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Живи с чувством. Как поставить цели, к которым лежит душа.txt' 'Психология/Живи с чувством. Как поставить цели, к которым лежит душа.txt' && echo "MOVED: Живи с чувством. Как поставить цели, к которым лежит душа.txt -> Психология" >> "$LOG" || echo "FAIL: Живи с чувством. Как поставить цели, к которым лежит душа.txt -> Психология" >> "$LOG"
fi
if [ -e 'Развитие/Жизнь_без_усилий_transcription.txt' ]; then
  echo "SKIP(exists): Жизнь_без_усилий_transcription.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Жизнь_без_усилий_transcription.txt' 'Развитие/Жизнь_без_усилий_transcription.txt' && echo "MOVED: Жизнь_без_усилий_transcription.txt -> Развитие" >> "$LOG" || echo "FAIL: Жизнь_без_усилий_transcription.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Здоровье/ЗОЖ оно вам надо.txt' ]; then
  echo "SKIP(exists): ЗОЖ оно вам надо.txt -> Здоровье" >> "$LOG"
else
  mv 'свободные_книги/ЗОЖ оно вам надо.txt' 'Здоровье/ЗОЖ оно вам надо.txt' && echo "MOVED: ЗОЖ оно вам надо.txt -> Здоровье" >> "$LOG" || echo "FAIL: ЗОЖ оно вам надо.txt -> Здоровье" >> "$LOG"
fi
if [ -e 'Продажи/Закрыть_сделку_Пять_навыков_для_отличных_результатов_в_продажах.mp3' ]; then
  echo "SKIP(exists): Закрыть_сделку_Пять_навыков_для_отличных_результатов_в_продажах.mp3 -> Продажи" >> "$LOG"
else
  mv 'свободные_книги/Закрыть_сделку_Пять_навыков_для_отличных_результатов_в_продажах.mp3' 'Продажи/Закрыть_сделку_Пять_навыков_для_отличных_результатов_в_продажах.mp3' && echo "MOVED: Закрыть_сделку_Пять_навыков_для_отличных_результатов_в_продажах.mp3 -> Продажи" >> "$LOG" || echo "FAIL: Закрыть_сделку_Пять_навыков_для_отличных_результатов_в_продажах.mp3 -> Продажи" >> "$LOG"
fi
if [ -e 'Здоровье/Зачем мы спим. Новая наука о сне и сновидениях - часть 1.txt' ]; then
  echo "SKIP(exists): Зачем мы спим. Новая наука о сне и сновидениях - часть 1.txt -> Здоровье" >> "$LOG"
else
  mv 'свободные_книги/Зачем мы спим. Новая наука о сне и сновидениях - часть 1.txt' 'Здоровье/Зачем мы спим. Новая наука о сне и сновидениях - часть 1.txt' && echo "MOVED: Зачем мы спим. Новая наука о сне и сновидениях - часть 1.txt -> Здоровье" >> "$LOG" || echo "FAIL: Зачем мы спим. Новая наука о сне и сновидениях - часть 1.txt -> Здоровье" >> "$LOG"
fi
if [ -e 'Здоровье/Зачем мы спим. Новая наука о сне и сновидениях - часть 2.txt' ]; then
  echo "SKIP(exists): Зачем мы спим. Новая наука о сне и сновидениях - часть 2.txt -> Здоровье" >> "$LOG"
else
  mv 'свободные_книги/Зачем мы спим. Новая наука о сне и сновидениях - часть 2.txt' 'Здоровье/Зачем мы спим. Новая наука о сне и сновидениях - часть 2.txt' && echo "MOVED: Зачем мы спим. Новая наука о сне и сновидениях - часть 2.txt -> Здоровье" >> "$LOG" || echo "FAIL: Зачем мы спим. Новая наука о сне и сновидениях - часть 2.txt -> Здоровье" >> "$LOG"
fi
if [ -e 'Психология/Здоровый мозг. Программа для улучшения памяти и мышления.txt' ]; then
  echo "SKIP(exists): Здоровый мозг. Программа для улучшения памяти и мышления.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Здоровый мозг. Программа для улучшения памяти и мышления.txt' 'Психология/Здоровый мозг. Программа для улучшения памяти и мышления.txt' && echo "MOVED: Здоровый мозг. Программа для улучшения памяти и мышления.txt -> Психология" >> "$LOG" || echo "FAIL: Здоровый мозг. Программа для улучшения памяти и мышления.txt -> Психология" >> "$LOG"
fi
if [ -e 'Психология/Идиотский бесценный мозг. Как мы поддаемся на все уловки и хитрости нашего мозга - часть 2.txt' ]; then
  echo "SKIP(exists): Идиотский бесценный мозг. Как мы поддаемся на все уловки и хитрости нашего мозга - часть 2.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Идиотский бесценный мозг. Как мы поддаемся на все уловки и хитрости нашего мозга - часть 2.txt' 'Психология/Идиотский бесценный мозг. Как мы поддаемся на все уловки и хитрости нашего мозга - часть 2.txt' && echo "MOVED: Идиотский бесценный мозг. Как мы поддаемся на все уловки и хитрости нашего мозга - часть 2.txt -> Психология" >> "$LOG" || echo "FAIL: Идиотский бесценный мозг. Как мы поддаемся на все уловки и хитрости нашего мозга - часть 2.txt -> Психология" >> "$LOG"
fi
if [ -e 'Психология/Идиотский бесценный мозг.txt' ]; then
  echo "SKIP(exists): Идиотский бесценный мозг.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Идиотский бесценный мозг.txt' 'Психология/Идиотский бесценный мозг.txt' && echo "MOVED: Идиотский бесценный мозг.txt -> Психология" >> "$LOG" || echo "FAIL: Идиотский бесценный мозг.txt -> Психология" >> "$LOG"
fi
if [ -e 'Развитие/Искусство видеть_transcription.txt' ]; then
  echo "SKIP(exists): Искусство видеть_transcription.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Искусство видеть_transcription.txt' 'Развитие/Искусство видеть_transcription.txt' && echo "MOVED: Искусство видеть_transcription.txt -> Развитие" >> "$LOG" || echo "FAIL: Искусство видеть_transcription.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Искусство правильно мыслить.txt' ]; then
  echo "SKIP(exists): Искусство правильно мыслить.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Искусство правильно мыслить.txt' 'Развитие/Искусство правильно мыслить.txt' && echo "MOVED: Искусство правильно мыслить.txt -> Развитие" >> "$LOG" || echo "FAIL: Искусство правильно мыслить.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Искусство продавать. Самые эффективные приемы и техники.txt' ]; then
  echo "SKIP(exists): Искусство продавать. Самые эффективные приемы и техники.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Искусство продавать. Самые эффективные приемы и техники.txt' 'Развитие/Искусство продавать. Самые эффективные приемы и техники.txt' && echo "MOVED: Искусство продавать. Самые эффективные приемы и техники.txt -> Развитие" >> "$LOG" || echo "FAIL: Искусство продавать. Самые эффективные приемы и техники.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Искусство продавать. Самые эффективные приемы и техники_transcription.txt' ]; then
  echo "SKIP(exists): Искусство продавать. Самые эффективные приемы и техники_transcription.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Искусство продавать. Самые эффективные приемы и техники_transcription.txt' 'Развитие/Искусство продавать. Самые эффективные приемы и техники_transcription.txt' && echo "MOVED: Искусство продавать. Самые эффективные приемы и техники_transcription.txt -> Развитие" >> "$LOG" || echo "FAIL: Искусство продавать. Самые эффективные приемы и техники_transcription.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Эзотерика, духовность/Йога и сексуальные практики - часть 1.txt' ]; then
  echo "SKIP(exists): Йога и сексуальные практики - часть 1.txt -> Эзотерика, духовность" >> "$LOG"
else
  mv 'свободные_книги/Йога и сексуальные практики - часть 1.txt' 'Эзотерика, духовность/Йога и сексуальные практики - часть 1.txt' && echo "MOVED: Йога и сексуальные практики - часть 1.txt -> Эзотерика, духовность" >> "$LOG" || echo "FAIL: Йога и сексуальные практики - часть 1.txt -> Эзотерика, духовность" >> "$LOG"
fi
if [ -e 'Развитие/К_черту_всё!_Берись_и_делай!_Полная_версия.txt' ]; then
  echo "SKIP(exists): К_черту_всё!_Берись_и_делай!_Полная_версия.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/К_черту_всё!_Берись_и_делай!_Полная_версия.txt' 'Развитие/К_черту_всё!_Берись_и_делай!_Полная_версия.txt' && echo "MOVED: К_черту_всё!_Берись_и_делай!_Полная_версия.txt -> Развитие" >> "$LOG" || echo "FAIL: К_черту_всё!_Берись_и_делай!_Полная_версия.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Как включить осознанность. Техники эффективных практик и медитаций в современном мире.txt' ]; then
  echo "SKIP(exists): Как включить осознанность. Техники эффективных практик и медитаций в современном мире.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Как включить осознанность. Техники эффективных практик и медитаций в современном мире.txt' 'Развитие/Как включить осознанность. Техники эффективных практик и медитаций в современном мире.txt' && echo "MOVED: Как включить осознанность. Техники эффективных практик и медитаций в современном мире.txt -> Развитие" >> "$LOG" || echo "FAIL: Как включить осознанность. Техники эффективных практик и медитаций в современном мире.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Как есть меньше. Преодолеваем пищевую зависимость.txt' ]; then
  echo "SKIP(exists): Как есть меньше. Преодолеваем пищевую зависимость.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Как есть меньше. Преодолеваем пищевую зависимость.txt' 'Развитие/Как есть меньше. Преодолеваем пищевую зависимость.txt' && echo "MOVED: Как есть меньше. Преодолеваем пищевую зависимость.txt -> Развитие" >> "$LOG" || echo "FAIL: Как есть меньше. Преодолеваем пищевую зависимость.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Эзотерика, духовность/Как любить осознанно.txt' ]; then
  echo "SKIP(exists): Как любить осознанно.txt -> Эзотерика, духовность" >> "$LOG"
else
  mv 'свободные_книги/Как любить осознанно.txt' 'Эзотерика, духовность/Как любить осознанно.txt' && echo "MOVED: Как любить осознанно.txt -> Эзотерика, духовность" >> "$LOG" || echo "FAIL: Как любить осознанно.txt -> Эзотерика, духовность" >> "$LOG"
fi
if [ -e 'Эзотерика, духовность/Как любить осознанно_transcription.txt' ]; then
  echo "SKIP(exists): Как любить осознанно_transcription.txt -> Эзотерика, духовность" >> "$LOG"
else
  mv 'свободные_книги/Как любить осознанно_transcription.txt' 'Эзотерика, духовность/Как любить осознанно_transcription.txt' && echo "MOVED: Как любить осознанно_transcription.txt -> Эзотерика, духовность" >> "$LOG" || echo "FAIL: Как любить осознанно_transcription.txt -> Эзотерика, духовность" >> "$LOG"
fi
if [ -e 'Психология/Как люди думают.txt' ]; then
  echo "SKIP(exists): Как люди думают.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Как люди думают.txt' 'Психология/Как люди думают.txt' && echo "MOVED: Как люди думают.txt -> Психология" >> "$LOG" || echo "FAIL: Как люди думают.txt -> Психология" >> "$LOG"
fi
if [ -e 'Общение, красноречие, голос/Как писать убедительно .txt' ]; then
  echo "SKIP(exists): Как писать убедительно .txt -> Общение, красноречие, голос" >> "$LOG"
else
  mv 'свободные_книги/Как писать убедительно .txt' 'Общение, красноречие, голос/Как писать убедительно .txt' && echo "MOVED: Как писать убедительно .txt -> Общение, красноречие, голос" >> "$LOG" || echo "FAIL: Как писать убедительно .txt -> Общение, красноречие, голос" >> "$LOG"
fi
if [ -e 'Общение, красноречие, голос/Как писать убедительно.txt' ]; then
  echo "SKIP(exists): Как писать убедительно.txt -> Общение, красноречие, голос" >> "$LOG"
else
  mv 'свободные_книги/Как писать убедительно.txt' 'Общение, красноречие, голос/Как писать убедительно.txt' && echo "MOVED: Как писать убедительно.txt -> Общение, красноречие, голос" >> "$LOG" || echo "FAIL: Как писать убедительно.txt -> Общение, красноречие, голос" >> "$LOG"
fi
if [ -e 'Тайм-менеджмент/Как привести дела в порядок. Искусство продуктивности без стресса - часть 1.txt' ]; then
  echo "SKIP(exists): Как привести дела в порядок. Искусство продуктивности без стресса - часть 1.txt -> Тайм-менеджмент" >> "$LOG"
else
  mv 'свободные_книги/Как привести дела в порядок. Искусство продуктивности без стресса - часть 1.txt' 'Тайм-менеджмент/Как привести дела в порядок. Искусство продуктивности без стресса - часть 1.txt' && echo "MOVED: Как привести дела в порядок. Искусство продуктивности без стресса - часть 1.txt -> Тайм-менеджмент" >> "$LOG" || echo "FAIL: Как привести дела в порядок. Искусство продуктивности без стресса - часть 1.txt -> Тайм-менеджмент" >> "$LOG"
fi
if [ -e 'Тайм-менеджмент/Как привести дела в порядок. Искусство продуктивности без стресса - часть 2.txt' ]; then
  echo "SKIP(exists): Как привести дела в порядок. Искусство продуктивности без стресса - часть 2.txt -> Тайм-менеджмент" >> "$LOG"
else
  mv 'свободные_книги/Как привести дела в порядок. Искусство продуктивности без стресса - часть 2.txt' 'Тайм-менеджмент/Как привести дела в порядок. Искусство продуктивности без стресса - часть 2.txt' && echo "MOVED: Как привести дела в порядок. Искусство продуктивности без стресса - часть 2.txt -> Тайм-менеджмент" >> "$LOG" || echo "FAIL: Как привести дела в порядок. Искусство продуктивности без стресса - часть 2.txt -> Тайм-менеджмент" >> "$LOG"
fi
if [ -e 'Развитие/Как_лгать_при_помощи_статистики.txt' ]; then
  echo "SKIP(exists): Как_лгать_при_помощи_статистики.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Как_лгать_при_помощи_статистики.txt' 'Развитие/Как_лгать_при_помощи_статистики.txt' && echo "MOVED: Как_лгать_при_помощи_статистики.txt -> Развитие" >> "$LOG" || echo "FAIL: Как_лгать_при_помощи_статистики.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Как_не_ошибаться1.txt' ]; then
  echo "SKIP(exists): Как_не_ошибаться1.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Как_не_ошибаться1.txt' 'Развитие/Как_не_ошибаться1.txt' && echo "MOVED: Как_не_ошибаться1.txt -> Развитие" >> "$LOG" || echo "FAIL: Как_не_ошибаться1.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Как_не_ошибаться2..txt' ]; then
  echo "SKIP(exists): Как_не_ошибаться2..txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Как_не_ошибаться2..txt' 'Развитие/Как_не_ошибаться2..txt' && echo "MOVED: Как_не_ошибаться2..txt -> Развитие" >> "$LOG" || echo "FAIL: Как_не_ошибаться2..txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Как_не_ошибаться3.txt' ]; then
  echo "SKIP(exists): Как_не_ошибаться3.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Как_не_ошибаться3.txt' 'Развитие/Как_не_ошибаться3.txt' && echo "MOVED: Как_не_ошибаться3.txt -> Развитие" >> "$LOG" || echo "FAIL: Как_не_ошибаться3.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Продажи/Книга_переговорщика_Гениальное_руководство_для_успешных_сделок.txt' ]; then
  echo "SKIP(exists): Книга_переговорщика_Гениальное_руководство_для_успешных_сделок.txt -> Продажи" >> "$LOG"
else
  mv 'свободные_книги/Книга_переговорщика_Гениальное_руководство_для_успешных_сделок.txt' 'Продажи/Книга_переговорщика_Гениальное_руководство_для_успешных_сделок.txt' && echo "MOVED: Книга_переговорщика_Гениальное_руководство_для_успешных_сделок.txt -> Продажи" >> "$LOG" || echo "FAIL: Книга_переговорщика_Гениальное_руководство_для_успешных_сделок.txt -> Продажи" >> "$LOG"
fi
if [ -e 'Развитие/Когда_грабить_банк_и_другие_лайфхаки.txt' ]; then
  echo "SKIP(exists): Когда_грабить_банк_и_другие_лайфхаки.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Когда_грабить_банк_и_другие_лайфхаки.txt' 'Развитие/Когда_грабить_банк_и_другие_лайфхаки.txt' && echo "MOVED: Когда_грабить_банк_и_другие_лайфхаки.txt -> Развитие" >> "$LOG" || echo "FAIL: Когда_грабить_банк_и_другие_лайфхаки.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Финансы/Количественная теория денег.txt' ]; then
  echo "SKIP(exists): Количественная теория денег.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Количественная теория денег.txt' 'Финансы/Количественная теория денег.txt' && echo "MOVED: Количественная теория денег.txt -> Финансы" >> "$LOG" || echo "FAIL: Количественная теория денег.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Развитие/Кофеман. Как найти.txt' ]; then
  echo "SKIP(exists): Кофеман. Как найти.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Кофеман. Как найти.txt' 'Развитие/Кофеман. Как найти.txt' && echo "MOVED: Кофеман. Как найти.txt -> Развитие" >> "$LOG" || echo "FAIL: Кофеман. Как найти.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Финансы/Кошелек_или_жизнь.txt' ]; then
  echo "SKIP(exists): Кошелек_или_жизнь.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Кошелек_или_жизнь.txt' 'Финансы/Кошелек_или_жизнь.txt' && echo "MOVED: Кошелек_или_жизнь.txt -> Финансы" >> "$LOG" || echo "FAIL: Кошелек_или_жизнь.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/Кошелек_или_жизнь2.txt' ]; then
  echo "SKIP(exists): Кошелек_или_жизнь2.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Кошелек_или_жизнь2.txt' 'Финансы/Кошелек_или_жизнь2.txt' && echo "MOVED: Кошелек_или_жизнь2.txt -> Финансы" >> "$LOG" || echo "FAIL: Кошелек_или_жизнь2.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/Краткая_история_денег.txt' ]; then
  echo "SKIP(exists): Краткая_история_денег.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Краткая_история_денег.txt' 'Финансы/Краткая_история_денег.txt' && echo "MOVED: Краткая_история_денег.txt -> Финансы" >> "$LOG" || echo "FAIL: Краткая_история_денег.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Развитие/Легкий_способ_добиться_успеха.txt' ]; then
  echo "SKIP(exists): Легкий_способ_добиться_успеха.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Легкий_способ_добиться_успеха.txt' 'Развитие/Легкий_способ_добиться_успеха.txt' && echo "MOVED: Легкий_способ_добиться_успеха.txt -> Развитие" >> "$LOG" || echo "FAIL: Легкий_способ_добиться_успеха.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Финансы/Личные финансы-2. Секреты управления и индивидуальный финансовый план.txt' ]; then
  echo "SKIP(exists): Личные финансы-2. Секреты управления и индивидуальный финансовый план.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Личные финансы-2. Секреты управления и индивидуальный финансовый план.txt' 'Финансы/Личные финансы-2. Секреты управления и индивидуальный финансовый план.txt' && echo "MOVED: Личные финансы-2. Секреты управления и индивидуальный финансовый план.txt -> Финансы" >> "$LOG" || echo "FAIL: Личные финансы-2. Секреты управления и индивидуальный финансовый план.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Развитие/Логика смысла (Вторая половина) - часть 1.txt' ]; then
  echo "SKIP(exists): Логика смысла (Вторая половина) - часть 1.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Логика смысла (Вторая половина) - часть 1.txt' 'Развитие/Логика смысла (Вторая половина) - часть 1.txt' && echo "MOVED: Логика смысла (Вторая половина) - часть 1.txt -> Развитие" >> "$LOG" || echo "FAIL: Логика смысла (Вторая половина) - часть 1.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Логика смысла (Вторая половина) - часть 2.txt' ]; then
  echo "SKIP(exists): Логика смысла (Вторая половина) - часть 2.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Логика смысла (Вторая половина) - часть 2.txt' 'Развитие/Логика смысла (Вторая половина) - часть 2.txt' && echo "MOVED: Логика смысла (Вторая половина) - часть 2.txt -> Развитие" >> "$LOG" || echo "FAIL: Логика смысла (Вторая половина) - часть 2.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Логика.txt' ]; then
  echo "SKIP(exists): Логика.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Логика.txt' 'Развитие/Логика.txt' && echo "MOVED: Логика.txt -> Развитие" >> "$LOG" || echo "FAIL: Логика.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Логика_Учебник_для_средней_школы_Издание_восьмое.txt' ]; then
  echo "SKIP(exists): Логика_Учебник_для_средней_школы_Издание_восьмое.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Логика_Учебник_для_средней_школы_Издание_восьмое.txt' 'Развитие/Логика_Учебник_для_средней_школы_Издание_восьмое.txt' && echo "MOVED: Логика_Учебник_для_средней_школы_Издание_восьмое.txt -> Развитие" >> "$LOG" || echo "FAIL: Логика_Учебник_для_средней_школы_Издание_восьмое.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Психология/Ложная память. Почему нельзя доверять воспоминаниям - часть 1..txt' ]; then
  echo "SKIP(exists): Ложная память. Почему нельзя доверять воспоминаниям - часть 1..txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Ложная память. Почему нельзя доверять воспоминаниям - часть 1..txt' 'Психология/Ложная память. Почему нельзя доверять воспоминаниям - часть 1..txt' && echo "MOVED: Ложная память. Почему нельзя доверять воспоминаниям - часть 1..txt -> Психология" >> "$LOG" || echo "FAIL: Ложная память. Почему нельзя доверять воспоминаниям - часть 1..txt -> Психология" >> "$LOG"
fi
if [ -e 'Развитие/Лучше_поздно,_чем_никогда.txt' ]; then
  echo "SKIP(exists): Лучше_поздно,_чем_никогда.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Лучше_поздно,_чем_никогда.txt' 'Развитие/Лучше_поздно,_чем_никогда.txt' && echo "MOVED: Лучше_поздно,_чем_никогда.txt -> Развитие" >> "$LOG" || echo "FAIL: Лучше_поздно,_чем_никогда.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Магия утра. Как первый час дня определяет ваш успех.txt' ]; then
  echo "SKIP(exists): Магия утра. Как первый час дня определяет ваш успех.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Магия утра. Как первый час дня определяет ваш успех.txt' 'Развитие/Магия утра. Как первый час дня определяет ваш успех.txt' && echo "MOVED: Магия утра. Как первый час дня определяет ваш успех.txt -> Развитие" >> "$LOG" || echo "FAIL: Магия утра. Как первый час дня определяет ваш успех.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Финансы/Мани, или Азбука денег.txt' ]; then
  echo "SKIP(exists): Мани, или Азбука денег.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Мани, или Азбука денег.txt' 'Финансы/Мани, или Азбука денег.txt' && echo "MOVED: Мани, или Азбука денег.txt -> Финансы" >> "$LOG" || echo "FAIL: Мани, или Азбука денег.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Бизнес, менеджмент/Маркетинг_от_А_до_Я_80_концепций.txt' ]; then
  echo "SKIP(exists): Маркетинг_от_А_до_Я_80_концепций.txt -> Бизнес, менеджмент" >> "$LOG"
else
  mv 'свободные_книги/Маркетинг_от_А_до_Я_80_концепций.txt' 'Бизнес, менеджмент/Маркетинг_от_А_до_Я_80_концепций.txt' && echo "MOVED: Маркетинг_от_А_до_Я_80_концепций.txt -> Бизнес, менеджмент" >> "$LOG" || echo "FAIL: Маркетинг_от_А_до_Я_80_концепций.txt -> Бизнес, менеджмент" >> "$LOG"
fi
if [ -e 'Развитие/Мастер-ключ_к_исполнению_желаний.txt' ]; then
  echo "SKIP(exists): Мастер-ключ_к_исполнению_желаний.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Мастер-ключ_к_исполнению_желаний.txt' 'Развитие/Мастер-ключ_к_исполнению_желаний.txt' && echo "MOVED: Мастер-ключ_к_исполнению_желаний.txt -> Развитие" >> "$LOG" || echo "FAIL: Мастер-ключ_к_исполнению_желаний.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Продажи/Мастер_больших_продаж_Искусство_заключать_крупные_контракты.txt' ]; then
  echo "SKIP(exists): Мастер_больших_продаж_Искусство_заключать_крупные_контракты.txt -> Продажи" >> "$LOG"
else
  mv 'свободные_книги/Мастер_больших_продаж_Искусство_заключать_крупные_контракты.txt' 'Продажи/Мастер_больших_продаж_Искусство_заключать_крупные_контракты.txt' && echo "MOVED: Мастер_больших_продаж_Искусство_заключать_крупные_контракты.txt -> Продажи" >> "$LOG" || echo "FAIL: Мастер_больших_продаж_Искусство_заключать_крупные_контракты.txt -> Продажи" >> "$LOG"
fi
if [ -e 'Развитие/Математика для взрослых.txt' ]; then
  echo "SKIP(exists): Математика для взрослых.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Математика для взрослых.txt' 'Развитие/Математика для взрослых.txt' && echo "MOVED: Математика для взрослых.txt -> Развитие" >> "$LOG" || echo "FAIL: Математика для взрослых.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Математика для взрослых_transcription.txt' ]; then
  echo "SKIP(exists): Математика для взрослых_transcription.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Математика для взрослых_transcription.txt' 'Развитие/Математика для взрослых_transcription.txt' && echo "MOVED: Математика для взрослых_transcription.txt -> Развитие" >> "$LOG" || echo "FAIL: Математика для взрослых_transcription.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Бизнес, менеджмент/Менеджер_мафии_Руководство_для_корпоративного.txt' ]; then
  echo "SKIP(exists): Менеджер_мафии_Руководство_для_корпоративного.txt -> Бизнес, менеджмент" >> "$LOG"
else
  mv 'свободные_книги/Менеджер_мафии_Руководство_для_корпоративного.txt' 'Бизнес, менеджмент/Менеджер_мафии_Руководство_для_корпоративного.txt' && echo "MOVED: Менеджер_мафии_Руководство_для_корпоративного.txt -> Бизнес, менеджмент" >> "$LOG" || echo "FAIL: Менеджер_мафии_Руководство_для_корпоративного.txt -> Бизнес, менеджмент" >> "$LOG"
fi
if [ -e 'Развитие/Мир_трех_нулей.txt' ]; then
  echo "SKIP(exists): Мир_трех_нулей.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Мир_трех_нулей.txt' 'Развитие/Мир_трех_нулей.txt' && echo "MOVED: Мир_трех_нулей.txt -> Развитие" >> "$LOG" || echo "FAIL: Мир_трех_нулей.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Психология/Мозг Тонкая настройка. Наша жизнь с точки зрения нейронауки - часть 1.txt' ]; then
  echo "SKIP(exists): Мозг Тонкая настройка. Наша жизнь с точки зрения нейронауки - часть 1.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Мозг Тонкая настройка. Наша жизнь с точки зрения нейронауки - часть 1.txt' 'Психология/Мозг Тонкая настройка. Наша жизнь с точки зрения нейронауки - часть 1.txt' && echo "MOVED: Мозг Тонкая настройка. Наша жизнь с точки зрения нейронауки - часть 1.txt -> Психология" >> "$LOG" || echo "FAIL: Мозг Тонкая настройка. Наша жизнь с точки зрения нейронауки - часть 1.txt -> Психология" >> "$LOG"
fi
if [ -e 'Психология/Мозг Тонкая настройка. Наша жизнь с точки зрения нейронауки - часть 2.txt' ]; then
  echo "SKIP(exists): Мозг Тонкая настройка. Наша жизнь с точки зрения нейронауки - часть 2.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Мозг Тонкая настройка. Наша жизнь с точки зрения нейронауки - часть 2.txt' 'Психология/Мозг Тонкая настройка. Наша жизнь с точки зрения нейронауки - часть 2.txt' && echo "MOVED: Мозг Тонкая настройка. Наша жизнь с точки зрения нейронауки - часть 2.txt -> Психология" >> "$LOG" || echo "FAIL: Мозг Тонкая настройка. Наша жизнь с точки зрения нейронауки - часть 2.txt -> Психология" >> "$LOG"
fi
if [ -e 'Психология/Мозг. Инструкция пользователя - часть 1.txt' ]; then
  echo "SKIP(exists): Мозг. Инструкция пользователя - часть 1.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Мозг. Инструкция пользователя - часть 1.txt' 'Психология/Мозг. Инструкция пользователя - часть 1.txt' && echo "MOVED: Мозг. Инструкция пользователя - часть 1.txt -> Психология" >> "$LOG" || echo "FAIL: Мозг. Инструкция пользователя - часть 1.txt -> Психология" >> "$LOG"
fi
if [ -e 'Развитие/Мозг_Ваша_личная_история.txt' ]; then
  echo "SKIP(exists): Мозг_Ваша_личная_история.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Мозг_Ваша_личная_история.txt' 'Развитие/Мозг_Ваша_личная_история.txt' && echo "MOVED: Мозг_Ваша_личная_история.txt -> Развитие" >> "$LOG" || echo "FAIL: Мозг_Ваша_личная_история.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Здоровье/Моложе с каждым годом. Как дожить до 100 лет бодрым, здоровым и счастливым - часть 1.txt' ]; then
  echo "SKIP(exists): Моложе с каждым годом. Как дожить до 100 лет бодрым, здоровым и счастливым - часть 1.txt -> Здоровье" >> "$LOG"
else
  mv 'свободные_книги/Моложе с каждым годом. Как дожить до 100 лет бодрым, здоровым и счастливым - часть 1.txt' 'Здоровье/Моложе с каждым годом. Как дожить до 100 лет бодрым, здоровым и счастливым - часть 1.txt' && echo "MOVED: Моложе с каждым годом. Как дожить до 100 лет бодрым, здоровым и счастливым - часть 1.txt -> Здоровье" >> "$LOG" || echo "FAIL: Моложе с каждым годом. Как дожить до 100 лет бодрым, здоровым и счастливым - часть 1.txt -> Здоровье" >> "$LOG"
fi
if [ -e 'Здоровье/Моложе с каждым годом. Как дожить до 100 лет бодрым, здоровым и счастливым - часть 2.txt' ]; then
  echo "SKIP(exists): Моложе с каждым годом. Как дожить до 100 лет бодрым, здоровым и счастливым - часть 2.txt -> Здоровье" >> "$LOG"
else
  mv 'свободные_книги/Моложе с каждым годом. Как дожить до 100 лет бодрым, здоровым и счастливым - часть 2.txt' 'Здоровье/Моложе с каждым годом. Как дожить до 100 лет бодрым, здоровым и счастливым - часть 2.txt' && echo "MOVED: Моложе с каждым годом. Как дожить до 100 лет бодрым, здоровым и счастливым - часть 2.txt -> Здоровье" >> "$LOG" || echo "FAIL: Моложе с каждым годом. Как дожить до 100 лет бодрым, здоровым и счастливым - часть 2.txt -> Здоровье" >> "$LOG"
fi
if [ -e 'Развитие/Музыка как предмет логики.txt' ]; then
  echo "SKIP(exists): Музыка как предмет логики.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Музыка как предмет логики.txt' 'Развитие/Музыка как предмет логики.txt' && echo "MOVED: Музыка как предмет логики.txt -> Развитие" >> "$LOG" || echo "FAIL: Музыка как предмет логики.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Тайм-менеджмент/Начни с главного!.mp3' ]; then
  echo "SKIP(exists): Начни с главного!.mp3 -> Тайм-менеджмент" >> "$LOG"
else
  mv 'свободные_книги/Начни с главного!.mp3' 'Тайм-менеджмент/Начни с главного!.mp3' && echo "MOVED: Начни с главного!.mp3 -> Тайм-менеджмент" >> "$LOG" || echo "FAIL: Начни с главного!.mp3 -> Тайм-менеджмент" >> "$LOG"
fi
if [ -e 'Развитие/Не навреди сам себе, - часть 1.txt' ]; then
  echo "SKIP(exists): Не навреди сам себе, - часть 1.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Не навреди сам себе, - часть 1.txt' 'Развитие/Не навреди сам себе, - часть 1.txt' && echo "MOVED: Не навреди сам себе, - часть 1.txt -> Развитие" >> "$LOG" || echo "FAIL: Не навреди сам себе, - часть 1.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Не навреди сам себе, - часть 2.txt' ]; then
  echo "SKIP(exists): Не навреди сам себе, - часть 2.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Не навреди сам себе, - часть 2.txt' 'Развитие/Не навреди сам себе, - часть 2.txt' && echo "MOVED: Не навреди сам себе, - часть 2.txt -> Развитие" >> "$LOG" || echo "FAIL: Не навреди сам себе, - часть 2.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Нейрокопирайтинг. 100+ приёмов влияния с помощью текста.txt' ]; then
  echo "SKIP(exists): Нейрокопирайтинг. 100+ приёмов влияния с помощью текста.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Нейрокопирайтинг. 100+ приёмов влияния с помощью текста.txt' 'Развитие/Нейрокопирайтинг. 100+ приёмов влияния с помощью текста.txt' && echo "MOVED: Нейрокопирайтинг. 100+ приёмов влияния с помощью текста.txt -> Развитие" >> "$LOG" || echo "FAIL: Нейрокопирайтинг. 100+ приёмов влияния с помощью текста.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Психология/Нестареющий мозг.txt' ]; then
  echo "SKIP(exists): Нестареющий мозг.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Нестареющий мозг.txt' 'Психология/Нестареющий мозг.txt' && echo "MOVED: Нестареющий мозг.txt -> Психология" >> "$LOG" || echo "FAIL: Нестареющий мозг.txt -> Психология" >> "$LOG"
fi
if [ -e 'Развитие/Нет оправданий! Сила самодисциплины.txt' ]; then
  echo "SKIP(exists): Нет оправданий! Сила самодисциплины.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Нет оправданий! Сила самодисциплины.txt' 'Развитие/Нет оправданий! Сила самодисциплины.txt' && echo "MOVED: Нет оправданий! Сила самодисциплины.txt -> Развитие" >> "$LOG" || echo "FAIL: Нет оправданий! Сила самодисциплины.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Одинокий город. Упражнения в искусстве одиночества - часть 1.txt' ]; then
  echo "SKIP(exists): Одинокий город. Упражнения в искусстве одиночества - часть 1.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Одинокий город. Упражнения в искусстве одиночества - часть 1.txt' 'Развитие/Одинокий город. Упражнения в искусстве одиночества - часть 1.txt' && echo "MOVED: Одинокий город. Упражнения в искусстве одиночества - часть 1.txt -> Развитие" >> "$LOG" || echo "FAIL: Одинокий город. Упражнения в искусстве одиночества - часть 1.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Одинокий город. Упражнения в искусстве одиночества - часть 2.txt' ]; then
  echo "SKIP(exists): Одинокий город. Упражнения в искусстве одиночества - часть 2.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Одинокий город. Упражнения в искусстве одиночества - часть 2.txt' 'Развитие/Одинокий город. Упражнения в искусстве одиночества - часть 2.txt' && echo "MOVED: Одинокий город. Упражнения в искусстве одиночества - часть 2.txt -> Развитие" >> "$LOG" || echo "FAIL: Одинокий город. Упражнения в искусстве одиночества - часть 2.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Опасные_желания.txt' ]; then
  echo "SKIP(exists): Опасные_желания.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Опасные_желания.txt' 'Развитие/Опасные_желания.txt' && echo "MOVED: Опасные_желания.txt -> Развитие" >> "$LOG" || echo "FAIL: Опасные_желания.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Оставьте брезгливость, съешьте лягушку!.txt' ]; then
  echo "SKIP(exists): Оставьте брезгливость, съешьте лягушку!.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Оставьте брезгливость, съешьте лягушку!.txt' 'Развитие/Оставьте брезгливость, съешьте лягушку!.txt' && echo "MOVED: Оставьте брезгливость, съешьте лягушку!.txt -> Развитие" >> "$LOG" || echo "FAIL: Оставьте брезгливость, съешьте лягушку!.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Оставьте брезгливость, съешьте лягушку!_transcription.txt' ]; then
  echo "SKIP(exists): Оставьте брезгливость, съешьте лягушку!_transcription.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Оставьте брезгливость, съешьте лягушку!_transcription.txt' 'Развитие/Оставьте брезгливость, съешьте лягушку!_transcription.txt' && echo "MOVED: Оставьте брезгливость, съешьте лягушку!_transcription.txt -> Развитие" >> "$LOG" || echo "FAIL: Оставьте брезгливость, съешьте лягушку!_transcription.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Бизнес, менеджмент/От Сунь-цзы до Стива Джобса искусство стратегии.txt' ]; then
  echo "SKIP(exists): От Сунь-цзы до Стива Джобса искусство стратегии.txt -> Бизнес, менеджмент" >> "$LOG"
else
  mv 'свободные_книги/От Сунь-цзы до Стива Джобса искусство стратегии.txt' 'Бизнес, менеджмент/От Сунь-цзы до Стива Джобса искусство стратегии.txt' && echo "MOVED: От Сунь-цзы до Стива Джобса искусство стратегии.txt -> Бизнес, менеджмент" >> "$LOG" || echo "FAIL: От Сунь-цзы до Стива Джобса искусство стратегии.txt -> Бизнес, менеджмент" >> "$LOG"
fi
if [ -e 'Бизнес, менеджмент/От нуля к единице. Как создать стартап, который изменит будущее..txt' ]; then
  echo "SKIP(exists): От нуля к единице. Как создать стартап, который изменит будущее..txt -> Бизнес, менеджмент" >> "$LOG"
else
  mv 'свободные_книги/От нуля к единице. Как создать стартап, который изменит будущее..txt' 'Бизнес, менеджмент/От нуля к единице. Как создать стартап, который изменит будущее..txt' && echo "MOVED: От нуля к единице. Как создать стартап, который изменит будущее..txt -> Бизнес, менеджмент" >> "$LOG" || echo "FAIL: От нуля к единице. Как создать стартап, который изменит будущее..txt -> Бизнес, менеджмент" >> "$LOG"
fi
if [ -e 'Развитие/От хорошего к великому - часть 1.txt' ]; then
  echo "SKIP(exists): От хорошего к великому - часть 1.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/От хорошего к великому - часть 1.txt' 'Развитие/От хорошего к великому - часть 1.txt' && echo "MOVED: От хорошего к великому - часть 1.txt -> Развитие" >> "$LOG" || echo "FAIL: От хорошего к великому - часть 1.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/От хорошего к великому - часть 2.txt' ]; then
  echo "SKIP(exists): От хорошего к великому - часть 2.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/От хорошего к великому - часть 2.txt' 'Развитие/От хорошего к великому - часть 2.txt' && echo "MOVED: От хорошего к великому - часть 2.txt -> Развитие" >> "$LOG" || echo "FAIL: От хорошего к великому - часть 2.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Здоровье/Очаровательный_кишечник.txt' ]; then
  echo "SKIP(exists): Очаровательный_кишечник.txt -> Здоровье" >> "$LOG"
else
  mv 'свободные_книги/Очаровательный_кишечник.txt' 'Здоровье/Очаровательный_кишечник.txt' && echo "MOVED: Очаровательный_кишечник.txt -> Здоровье" >> "$LOG" || echo "FAIL: Очаровательный_кишечник.txt -> Здоровье" >> "$LOG"
fi
if [ -e 'Развитие/Питание_как_основа_здоровья.txt' ]; then
  echo "SKIP(exists): Питание_как_основа_здоровья.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Питание_как_основа_здоровья.txt' 'Развитие/Питание_как_основа_здоровья.txt' && echo "MOVED: Питание_как_основа_здоровья.txt -> Развитие" >> "$LOG" || echo "FAIL: Питание_как_основа_здоровья.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Питание_как_основа_здоровья2.txt' ]; then
  echo "SKIP(exists): Питание_как_основа_здоровья2.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Питание_как_основа_здоровья2.txt' 'Развитие/Питание_как_основа_здоровья2.txt' && echo "MOVED: Питание_как_основа_здоровья2.txt -> Развитие" >> "$LOG" || echo "FAIL: Питание_как_основа_здоровья2.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Здоровье/Пить_или_не_пить_Новая_наука_об_алкоголе_и_вашем_здоровье.txt' ]; then
  echo "SKIP(exists): Пить_или_не_пить_Новая_наука_об_алкоголе_и_вашем_здоровье.txt -> Здоровье" >> "$LOG"
else
  mv 'свободные_книги/Пить_или_не_пить_Новая_наука_об_алкоголе_и_вашем_здоровье.txt' 'Здоровье/Пить_или_не_пить_Новая_наука_об_алкоголе_и_вашем_здоровье.txt' && echo "MOVED: Пить_или_не_пить_Новая_наука_об_алкоголе_и_вашем_здоровье.txt -> Здоровье" >> "$LOG" || echo "FAIL: Пить_или_не_пить_Новая_наука_об_алкоголе_и_вашем_здоровье.txt -> Здоровье" >> "$LOG"
fi
if [ -e 'Финансы/Поднимите свой финансовый IQ.txt' ]; then
  echo "SKIP(exists): Поднимите свой финансовый IQ.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Поднимите свой финансовый IQ.txt' 'Финансы/Поднимите свой финансовый IQ.txt' && echo "MOVED: Поднимите свой финансовый IQ.txt -> Финансы" >> "$LOG" || echo "FAIL: Поднимите свой финансовый IQ.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Здоровье/Полюби_другую_еду_–_улучши_тело_и_работу_мозга.txt' ]; then
  echo "SKIP(exists): Полюби_другую_еду_–_улучши_тело_и_работу_мозга.txt -> Здоровье" >> "$LOG"
else
  mv 'свободные_книги/Полюби_другую_еду_–_улучши_тело_и_работу_мозга.txt' 'Здоровье/Полюби_другую_еду_–_улучши_тело_и_работу_мозга.txt' && echo "MOVED: Полюби_другую_еду_–_улучши_тело_и_работу_мозга.txt -> Здоровье" >> "$LOG" || echo "FAIL: Полюби_другую_еду_–_улучши_тело_и_работу_мозга.txt -> Здоровье" >> "$LOG"
fi
if [ -e 'Развитие/Почему мужчина должен быть хорошо одет_transcription.txt' ]; then
  echo "SKIP(exists): Почему мужчина должен быть хорошо одет_transcription.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Почему мужчина должен быть хорошо одет_transcription.txt' 'Развитие/Почему мужчина должен быть хорошо одет_transcription.txt' && echo "MOVED: Почему мужчина должен быть хорошо одет_transcription.txt -> Развитие" >> "$LOG" || echo "FAIL: Почему мужчина должен быть хорошо одет_transcription.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Финансы/Почему одни страны богатые, а другие бедные - часть 1.txt' ]; then
  echo "SKIP(exists): Почему одни страны богатые, а другие бедные - часть 1.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Почему одни страны богатые, а другие бедные - часть 1.txt' 'Финансы/Почему одни страны богатые, а другие бедные - часть 1.txt' && echo "MOVED: Почему одни страны богатые, а другие бедные - часть 1.txt -> Финансы" >> "$LOG" || echo "FAIL: Почему одни страны богатые, а другие бедные - часть 1.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/Почему одни страны богатые, а другие бедные - часть 2.txt' ]; then
  echo "SKIP(exists): Почему одни страны богатые, а другие бедные - часть 2.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Почему одни страны богатые, а другие бедные - часть 2.txt' 'Финансы/Почему одни страны богатые, а другие бедные - часть 2.txt' && echo "MOVED: Почему одни страны богатые, а другие бедные - часть 2.txt -> Финансы" >> "$LOG" || echo "FAIL: Почему одни страны богатые, а другие бедные - часть 2.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/Почему одни страны богатые, а другие бедные - часть 3..txt' ]; then
  echo "SKIP(exists): Почему одни страны богатые, а другие бедные - часть 3..txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Почему одни страны богатые, а другие бедные - часть 3..txt' 'Финансы/Почему одни страны богатые, а другие бедные - часть 3..txt' && echo "MOVED: Почему одни страны богатые, а другие бедные - часть 3..txt -> Финансы" >> "$LOG" || echo "FAIL: Почему одни страны богатые, а другие бедные - часть 3..txt -> Финансы" >> "$LOG"
fi
if [ -e 'Развитие/Почему_E=mc²_И_почему_это_должно_нас_волновать.txt' ]; then
  echo "SKIP(exists): Почему_E=mc²_И_почему_это_должно_нас_волновать.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Почему_E=mc²_И_почему_это_должно_нас_волновать.txt' 'Развитие/Почему_E=mc²_И_почему_это_должно_нас_волновать.txt' && echo "MOVED: Почему_E=mc²_И_почему_это_должно_нас_волновать.txt -> Развитие" >> "$LOG" || echo "FAIL: Почему_E=mc²_И_почему_это_должно_нас_волновать.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Психология/Правила мозга. Что стоит знать о мозге вам и вашим детям.txt' ]; then
  echo "SKIP(exists): Правила мозга. Что стоит знать о мозге вам и вашим детям.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Правила мозга. Что стоит знать о мозге вам и вашим детям.txt' 'Психология/Правила мозга. Что стоит знать о мозге вам и вашим детям.txt' && echo "MOVED: Правила мозга. Что стоит знать о мозге вам и вашим детям.txt -> Психология" >> "$LOG" || echo "FAIL: Правила мозга. Что стоит знать о мозге вам и вашим детям.txt -> Психология" >> "$LOG"
fi
if [ -e 'Психология/Предрассудки о здоровье. Жить надо с умом и правильно - часть 1.txt' ]; then
  echo "SKIP(exists): Предрассудки о здоровье. Жить надо с умом и правильно - часть 1.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Предрассудки о здоровье. Жить надо с умом и правильно - часть 1.txt' 'Психология/Предрассудки о здоровье. Жить надо с умом и правильно - часть 1.txt' && echo "MOVED: Предрассудки о здоровье. Жить надо с умом и правильно - часть 1.txt -> Психология" >> "$LOG" || echo "FAIL: Предрассудки о здоровье. Жить надо с умом и правильно - часть 1.txt -> Психология" >> "$LOG"
fi
if [ -e 'Психология/Предрассудки о здоровье.txt' ]; then
  echo "SKIP(exists): Предрассудки о здоровье.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Предрассудки о здоровье.txt' 'Психология/Предрассудки о здоровье.txt' && echo "MOVED: Предрассудки о здоровье.txt -> Психология" >> "$LOG" || echo "FAIL: Предрассудки о здоровье.txt -> Психология" >> "$LOG"
fi
if [ -e 'Психология/Привычка достигать. Как применять дизайн-мышление для достижения целей, которые казались вам невозможными.txt' ]; then
  echo "SKIP(exists): Привычка достигать. Как применять дизайн-мышление для достижения целей, которые казались вам невозможными.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Привычка достигать. Как применять дизайн-мышление для достижения целей, которые казались вам невозможными.txt' 'Психология/Привычка достигать. Как применять дизайн-мышление для достижения целей, которые казались вам невозможными.txt' && echo "MOVED: Привычка достигать. Как применять дизайн-мышление для достижения целей, которые казались вам невозможными.txt -> Психология" >> "$LOG" || echo "FAIL: Привычка достигать. Как применять дизайн-мышление для достижения целей, которые казались вам невозможными.txt -> Психология" >> "$LOG"
fi
if [ -e 'Финансы/Принципы. Жизнь и работа - часть 1.txt' ]; then
  echo "SKIP(exists): Принципы. Жизнь и работа - часть 1.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Принципы. Жизнь и работа - часть 1.txt' 'Финансы/Принципы. Жизнь и работа - часть 1.txt' && echo "MOVED: Принципы. Жизнь и работа - часть 1.txt -> Финансы" >> "$LOG" || echo "FAIL: Принципы. Жизнь и работа - часть 1.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/Принципы. Жизнь и работа - часть 2.txt' ]; then
  echo "SKIP(exists): Принципы. Жизнь и работа - часть 2.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Принципы. Жизнь и работа - часть 2.txt' 'Финансы/Принципы. Жизнь и работа - часть 2.txt' && echo "MOVED: Принципы. Жизнь и работа - часть 2.txt -> Финансы" >> "$LOG" || echo "FAIL: Принципы. Жизнь и работа - часть 2.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Развитие/Принципы_жизни.txt' ]; then
  echo "SKIP(exists): Принципы_жизни.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Принципы_жизни.txt' 'Развитие/Принципы_жизни.txt' && echo "MOVED: Принципы_жизни.txt -> Развитие" >> "$LOG" || echo "FAIL: Принципы_жизни.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Психология/Прокачай мозг методом британских ученых_transcription.txt' ]; then
  echo "SKIP(exists): Прокачай мозг методом британских ученых_transcription.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Прокачай мозг методом британских ученых_transcription.txt' 'Психология/Прокачай мозг методом британских ученых_transcription.txt' && echo "MOVED: Прокачай мозг методом британских ученых_transcription.txt -> Психология" >> "$LOG" || echo "FAIL: Прокачай мозг методом британских ученых_transcription.txt -> Психология" >> "$LOG"
fi
if [ -e 'Развитие/Проклятие наличности - часть 1.txt' ]; then
  echo "SKIP(exists): Проклятие наличности - часть 1.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Проклятие наличности - часть 1.txt' 'Развитие/Проклятие наличности - часть 1.txt' && echo "MOVED: Проклятие наличности - часть 1.txt -> Развитие" >> "$LOG" || echo "FAIL: Проклятие наличности - часть 1.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Проклятие наличности - часть 2.txt' ]; then
  echo "SKIP(exists): Проклятие наличности - часть 2.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Проклятие наличности - часть 2.txt' 'Развитие/Проклятие наличности - часть 2.txt' && echo "MOVED: Проклятие наличности - часть 2.txt -> Развитие" >> "$LOG" || echo "FAIL: Проклятие наличности - часть 2.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Финансы/Психология денег. Вечные уроки богатства, жадности и счастья.txt' ]; then
  echo "SKIP(exists): Психология денег. Вечные уроки богатства, жадности и счастья.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Психология денег. Вечные уроки богатства, жадности и счастья.txt' 'Финансы/Психология денег. Вечные уроки богатства, жадности и счастья.txt' && echo "MOVED: Психология денег. Вечные уроки богатства, жадности и счастья.txt -> Финансы" >> "$LOG" || echo "FAIL: Психология денег. Вечные уроки богатства, жадности и счастья.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Продажи/Психология убеждения. 50 доказанных способов быть убедительным.txt' ]; then
  echo "SKIP(exists): Психология убеждения. 50 доказанных способов быть убедительным.txt -> Продажи" >> "$LOG"
else
  mv 'свободные_книги/Психология убеждения. 50 доказанных способов быть убедительным.txt' 'Продажи/Психология убеждения. 50 доказанных способов быть убедительным.txt' && echo "MOVED: Психология убеждения. 50 доказанных способов быть убедительным.txt -> Продажи" >> "$LOG" || echo "FAIL: Психология убеждения. 50 доказанных способов быть убедительным.txt -> Продажи" >> "$LOG"
fi
if [ -e 'Психология/Психология_влияния.txt' ]; then
  echo "SKIP(exists): Психология_влияния.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Психология_влияния.txt' 'Психология/Психология_влияния.txt' && echo "MOVED: Психология_влияния.txt -> Психология" >> "$LOG" || echo "FAIL: Психология_влияния.txt -> Психология" >> "$LOG"
fi
if [ -e 'Психология/Психология_влияния2.txt' ]; then
  echo "SKIP(exists): Психология_влияния2.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Психология_влияния2.txt' 'Психология/Психология_влияния2.txt' && echo "MOVED: Психология_влияния2.txt -> Психология" >> "$LOG" || echo "FAIL: Психология_влияния2.txt -> Психология" >> "$LOG"
fi
if [ -e 'Развитие/Путешествие_еды.txt' ]; then
  echo "SKIP(exists): Путешествие_еды.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Путешествие_еды.txt' 'Развитие/Путешествие_еды.txt' && echo "MOVED: Путешествие_еды.txt -> Развитие" >> "$LOG" || echo "FAIL: Путешествие_еды.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Путешествие_еды2.txt' ]; then
  echo "SKIP(exists): Путешествие_еды2.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Путешествие_еды2.txt' 'Развитие/Путешествие_еды2.txt' && echo "MOVED: Путешествие_еды2.txt -> Развитие" >> "$LOG" || echo "FAIL: Путешествие_еды2.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Пути_в_незнаемое.txt' ]; then
  echo "SKIP(exists): Пути_в_незнаемое.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Пути_в_незнаемое.txt' 'Развитие/Пути_в_незнаемое.txt' && echo "MOVED: Пути_в_незнаемое.txt -> Развитие" >> "$LOG" || echo "FAIL: Пути_в_незнаемое.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Пути_в_незнаемое2.txt' ]; then
  echo "SKIP(exists): Пути_в_незнаемое2.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Пути_в_незнаемое2.txt' 'Развитие/Пути_в_незнаемое2.txt' && echo "MOVED: Пути_в_незнаемое2.txt -> Развитие" >> "$LOG" || echo "FAIL: Пути_в_незнаемое2.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Пути_в_незнаемое3.txt' ]; then
  echo "SKIP(exists): Пути_в_незнаемое3.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Пути_в_незнаемое3.txt' 'Развитие/Пути_в_незнаемое3.txt' && echo "MOVED: Пути_в_незнаемое3.txt -> Развитие" >> "$LOG" || echo "FAIL: Пути_в_незнаемое3.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Радикальная_неопределенность_Принятие_решений_за_пределами_цифр.txt' ]; then
  echo "SKIP(exists): Радикальная_неопределенность_Принятие_решений_за_пределами_цифр.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Радикальная_неопределенность_Принятие_решений_за_пределами_цифр.txt' 'Развитие/Радикальная_неопределенность_Принятие_решений_за_пределами_цифр.txt' && echo "MOVED: Радикальная_неопределенность_Принятие_решений_за_пределами_цифр.txt -> Развитие" >> "$LOG" || echo "FAIL: Радикальная_неопределенность_Принятие_решений_за_пределами_цифр.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Радикальная_неопределенность_Принятие_решений_за_пределами_цифр2.txt' ]; then
  echo "SKIP(exists): Радикальная_неопределенность_Принятие_решений_за_пределами_цифр2.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Радикальная_неопределенность_Принятие_решений_за_пределами_цифр2.txt' 'Развитие/Радикальная_неопределенность_Принятие_решений_за_пределами_цифр2.txt' && echo "MOVED: Радикальная_неопределенность_Принятие_решений_за_пределами_цифр2.txt -> Развитие" >> "$LOG" || echo "FAIL: Радикальная_неопределенность_Принятие_решений_за_пределами_цифр2.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Общение, красноречие, голос/Речь_против_языка_transcription.txt' ]; then
  echo "SKIP(exists): Речь_против_языка_transcription.txt -> Общение, красноречие, голос" >> "$LOG"
else
  mv 'свободные_книги/Речь_против_языка_transcription.txt' 'Общение, красноречие, голос/Речь_против_языка_transcription.txt' && echo "MOVED: Речь_против_языка_transcription.txt -> Общение, красноречие, голос" >> "$LOG" || echo "FAIL: Речь_против_языка_transcription.txt -> Общение, красноречие, голос" >> "$LOG"
fi
if [ -e 'Развитие/Сверху_вниз.txt' ]; then
  echo "SKIP(exists): Сверху_вниз.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Сверху_вниз.txt' 'Развитие/Сверху_вниз.txt' && echo "MOVED: Сверху_вниз.txt -> Развитие" >> "$LOG" || echo "FAIL: Сверху_вниз.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Свобода выбирать.txt' ]; then
  echo "SKIP(exists): Свобода выбирать.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Свобода выбирать.txt' 'Развитие/Свобода выбирать.txt' && echo "MOVED: Свобода выбирать.txt -> Развитие" >> "$LOG" || echo "FAIL: Свобода выбирать.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Свобода_выбирать_(fb2.txt' ]; then
  echo "SKIP(exists): Свобода_выбирать_(fb2.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Свобода_выбирать_(fb2.txt' 'Развитие/Свобода_выбирать_(fb2.txt' && echo "MOVED: Свобода_выбирать_(fb2.txt -> Развитие" >> "$LOG" || echo "FAIL: Свобода_выбирать_(fb2.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Психология/Семь грехов памяти. Как наш мозг нас обманывает - часть 1.txt' ]; then
  echo "SKIP(exists): Семь грехов памяти. Как наш мозг нас обманывает - часть 1.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Семь грехов памяти. Как наш мозг нас обманывает - часть 1.txt' 'Психология/Семь грехов памяти. Как наш мозг нас обманывает - часть 1.txt' && echo "MOVED: Семь грехов памяти. Как наш мозг нас обманывает - часть 1.txt -> Психология" >> "$LOG" || echo "FAIL: Семь грехов памяти. Как наш мозг нас обманывает - часть 1.txt -> Психология" >> "$LOG"
fi
if [ -e 'Психология/Семь грехов памяти. Как наш мозг нас обманывает - часть 2.txt' ]; then
  echo "SKIP(exists): Семь грехов памяти. Как наш мозг нас обманывает - часть 2.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Семь грехов памяти. Как наш мозг нас обманывает - часть 2.txt' 'Психология/Семь грехов памяти. Как наш мозг нас обманывает - часть 2.txt' && echo "MOVED: Семь грехов памяти. Как наш мозг нас обманывает - часть 2.txt -> Психология" >> "$LOG" || echo "FAIL: Семь грехов памяти. Как наш мозг нас обманывает - часть 2.txt -> Психология" >> "$LOG"
fi
if [ -e 'Развитие/Сила_влияния.txt' ]; then
  echo "SKIP(exists): Сила_влияния.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Сила_влияния.txt' 'Развитие/Сила_влияния.txt' && echo "MOVED: Сила_влияния.txt -> Развитие" >> "$LOG" || echo "FAIL: Сила_влияния.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Продажи/Слово_за_слово_искусство_переговоров_в_реальной_жизни.mp3' ]; then
  echo "SKIP(exists): Слово_за_слово_искусство_переговоров_в_реальной_жизни.mp3 -> Продажи" >> "$LOG"
else
  mv 'свободные_книги/Слово_за_слово_искусство_переговоров_в_реальной_жизни.mp3' 'Продажи/Слово_за_слово_искусство_переговоров_в_реальной_жизни.mp3' && echo "MOVED: Слово_за_слово_искусство_переговоров_в_реальной_жизни.mp3 -> Продажи" >> "$LOG" || echo "FAIL: Слово_за_слово_искусство_переговоров_в_реальной_жизни.mp3 -> Продажи" >> "$LOG"
fi
if [ -e 'Здоровье/Совершенное_тело_за_4_часа.txt' ]; then
  echo "SKIP(exists): Совершенное_тело_за_4_часа.txt -> Здоровье" >> "$LOG"
else
  mv 'свободные_книги/Совершенное_тело_за_4_часа.txt' 'Здоровье/Совершенное_тело_за_4_часа.txt' && echo "MOVED: Совершенное_тело_за_4_часа.txt -> Здоровье" >> "$LOG" || echo "FAIL: Совершенное_тело_за_4_часа.txt -> Здоровье" >> "$LOG"
fi
if [ -e 'Здоровье/Совершенное_тело_за_4_часа2.txt' ]; then
  echo "SKIP(exists): Совершенное_тело_за_4_часа2.txt -> Здоровье" >> "$LOG"
else
  mv 'свободные_книги/Совершенное_тело_за_4_часа2.txt' 'Здоровье/Совершенное_тело_за_4_часа2.txt' && echo "MOVED: Совершенное_тело_за_4_часа2.txt -> Здоровье" >> "$LOG" || echo "FAIL: Совершенное_тело_за_4_часа2.txt -> Здоровье" >> "$LOG"
fi
if [ -e 'Здоровье/Совершенное_тело_за_4_часа3.txt' ]; then
  echo "SKIP(exists): Совершенное_тело_за_4_часа3.txt -> Здоровье" >> "$LOG"
else
  mv 'свободные_книги/Совершенное_тело_за_4_часа3.txt' 'Здоровье/Совершенное_тело_за_4_часа3.txt' && echo "MOVED: Совершенное_тело_за_4_часа3.txt -> Здоровье" >> "$LOG" || echo "FAIL: Совершенное_тело_за_4_часа3.txt -> Здоровье" >> "$LOG"
fi
if [ -e 'Психология/Сознание_и_мозг.txt' ]; then
  echo "SKIP(exists): Сознание_и_мозг.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Сознание_и_мозг.txt' 'Психология/Сознание_и_мозг.txt' && echo "MOVED: Сознание_и_мозг.txt -> Психология" >> "$LOG" || echo "FAIL: Сознание_и_мозг.txt -> Психология" >> "$LOG"
fi
if [ -e 'Психология/Сознание_и_мозг2.txt' ]; then
  echo "SKIP(exists): Сознание_и_мозг2.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Сознание_и_мозг2.txt' 'Психология/Сознание_и_мозг2.txt' && echo "MOVED: Сознание_и_мозг2.txt -> Психология" >> "$LOG" || echo "FAIL: Сознание_и_мозг2.txt -> Психология" >> "$LOG"
fi
if [ -e 'Развитие/Справедливость.txt' ]; then
  echo "SKIP(exists): Справедливость.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Справедливость.txt' 'Развитие/Справедливость.txt' && echo "MOVED: Справедливость.txt -> Развитие" >> "$LOG" || echo "FAIL: Справедливость.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Справедливость2.txt' ]; then
  echo "SKIP(exists): Справедливость2.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Справедливость2.txt' 'Развитие/Справедливость2.txt' && echo "MOVED: Справедливость2.txt -> Развитие" >> "$LOG" || echo "FAIL: Справедливость2.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Странности нашего языка_transcription.txt' ]; then
  echo "SKIP(exists): Странности нашего языка_transcription.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Странности нашего языка_transcription.txt' 'Развитие/Странности нашего языка_transcription.txt' && echo "MOVED: Странности нашего языка_transcription.txt -> Развитие" >> "$LOG" || echo "FAIL: Странности нашего языка_transcription.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Тайм-менеджмент/Счастье уроки новой науки - часть 2.txt' ]; then
  echo "SKIP(exists): Счастье уроки новой науки - часть 2.txt -> Тайм-менеджмент" >> "$LOG"
else
  mv 'свободные_книги/Счастье уроки новой науки - часть 2.txt' 'Тайм-менеджмент/Счастье уроки новой науки - часть 2.txt' && echo "MOVED: Счастье уроки новой науки - часть 2.txt -> Тайм-менеджмент" >> "$LOG" || echo "FAIL: Счастье уроки новой науки - часть 2.txt -> Тайм-менеджмент" >> "$LOG"
fi
if [ -e 'Развитие/Тезаурус_вкусов.txt' ]; then
  echo "SKIP(exists): Тезаурус_вкусов.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Тезаурус_вкусов.txt' 'Развитие/Тезаурус_вкусов.txt' && echo "MOVED: Тезаурус_вкусов.txt -> Развитие" >> "$LOG" || echo "FAIL: Тезаурус_вкусов.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Психология/Теория игр. Искусство стратегического мышления в бизнесе и жизни - часть 2.txt' ]; then
  echo "SKIP(exists): Теория игр. Искусство стратегического мышления в бизнесе и жизни - часть 2.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Теория игр. Искусство стратегического мышления в бизнесе и жизни - часть 2.txt' 'Психология/Теория игр. Искусство стратегического мышления в бизнесе и жизни - часть 2.txt' && echo "MOVED: Теория игр. Искусство стратегического мышления в бизнесе и жизни - часть 2.txt -> Психология" >> "$LOG" || echo "FAIL: Теория игр. Искусство стратегического мышления в бизнесе и жизни - часть 2.txt -> Психология" >> "$LOG"
fi
if [ -e 'Развитие/Тестостерон_гормон,_который_разделяет_и_властвует.txt' ]; then
  echo "SKIP(exists): Тестостерон_гормон,_который_разделяет_и_властвует.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Тестостерон_гормон,_который_разделяет_и_властвует.txt' 'Развитие/Тестостерон_гормон,_который_разделяет_и_властвует.txt' && echo "MOVED: Тестостерон_гормон,_который_разделяет_и_властвует.txt -> Развитие" >> "$LOG" || echo "FAIL: Тестостерон_гормон,_который_разделяет_и_властвует.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Тестостерон_гормон,_который_разделяет_и_властвует2.txt' ]; then
  echo "SKIP(exists): Тестостерон_гормон,_который_разделяет_и_властвует2.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Тестостерон_гормон,_который_разделяет_и_властвует2.txt' 'Развитие/Тестостерон_гормон,_который_разделяет_и_властвует2.txt' && echo "MOVED: Тестостерон_гормон,_который_разделяет_и_властвует2.txt -> Развитие" >> "$LOG" || echo "FAIL: Тестостерон_гормон,_который_разделяет_и_властвует2.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Здоровье/Техника_тренировки_памяти.txt' ]; then
  echo "SKIP(exists): Техника_тренировки_памяти.txt -> Здоровье" >> "$LOG"
else
  mv 'свободные_книги/Техника_тренировки_памяти.txt' 'Здоровье/Техника_тренировки_памяти.txt' && echo "MOVED: Техника_тренировки_памяти.txt -> Здоровье" >> "$LOG" || echo "FAIL: Техника_тренировки_памяти.txt -> Здоровье" >> "$LOG"
fi
if [ -e 'Развитие/Удивительная_логика.txt' ]; then
  echo "SKIP(exists): Удивительная_логика.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Удивительная_логика.txt' 'Развитие/Удивительная_логика.txt' && echo "MOVED: Удивительная_логика.txt -> Развитие" >> "$LOG" || echo "FAIL: Удивительная_логика.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Удовольствие_от_X.txt' ]; then
  echo "SKIP(exists): Удовольствие_от_X.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Удовольствие_от_X.txt' 'Развитие/Удовольствие_от_X.txt' && echo "MOVED: Удовольствие_от_X.txt -> Развитие" >> "$LOG" || echo "FAIL: Удовольствие_от_X.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Психология/Ум во благо.txt' ]; then
  echo "SKIP(exists): Ум во благо.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Ум во благо.txt' 'Психология/Ум во благо.txt' && echo "MOVED: Ум во благо.txt -> Психология" >> "$LOG" || echo "FAIL: Ум во благо.txt -> Психология" >> "$LOG"
fi
if [ -e 'Финансы/Уоррен_Баффет.txt' ]; then
  echo "SKIP(exists): Уоррен_Баффет.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/Уоррен_Баффет.txt' 'Финансы/Уоррен_Баффет.txt' && echo "MOVED: Уоррен_Баффет.txt -> Финансы" >> "$LOG" || echo "FAIL: Уоррен_Баффет.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Развитие/Фильтру!Как работают наши печень и почки.txt' ]; then
  echo "SKIP(exists): Фильтру!Как работают наши печень и почки.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Фильтру!Как работают наши печень и почки.txt' 'Развитие/Фильтру!Как работают наши печень и почки.txt' && echo "MOVED: Фильтру!Как работают наши печень и почки.txt -> Развитие" >> "$LOG" || echo "FAIL: Фильтру!Как работают наши печень и почки.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/ХОЧУ… выглядеть стильно! Как улучшить свой гардероб и изменить жизнь.txt' ]; then
  echo "SKIP(exists): ХОЧУ… выглядеть стильно! Как улучшить свой гардероб и изменить жизнь.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/ХОЧУ… выглядеть стильно! Как улучшить свой гардероб и изменить жизнь.txt' 'Развитие/ХОЧУ… выглядеть стильно! Как улучшить свой гардероб и изменить жизнь.txt' && echo "MOVED: ХОЧУ… выглядеть стильно! Как улучшить свой гардероб и изменить жизнь.txt -> Развитие" >> "$LOG" || echo "FAIL: ХОЧУ… выглядеть стильно! Как улучшить свой гардероб и изменить жизнь.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Цифры_врут.txt' ]; then
  echo "SKIP(exists): Цифры_врут.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Цифры_врут.txt' 'Развитие/Цифры_врут.txt' && echo "MOVED: Цифры_врут.txt -> Развитие" >> "$LOG" || echo "FAIL: Цифры_врут.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Эзотерика, духовность/Человек уставший. Как победить хроническую усталость и вернуть себе силы, энергию и радость жизни.txt' ]; then
  echo "SKIP(exists): Человек уставший. Как победить хроническую усталость и вернуть себе силы, энергию и радость жизни.txt -> Эзотерика, духовность" >> "$LOG"
else
  mv 'свободные_книги/Человек уставший. Как победить хроническую усталость и вернуть себе силы, энергию и радость жизни.txt' 'Эзотерика, духовность/Человек уставший. Как победить хроническую усталость и вернуть себе силы, энергию и радость жизни.txt' && echo "MOVED: Человек уставший. Как победить хроническую усталость и вернуть себе силы, энергию и радость жизни.txt -> Эзотерика, духовность" >> "$LOG" || echo "FAIL: Человек уставший. Как победить хроническую усталость и вернуть себе силы, энергию и радость жизни.txt -> Эзотерика, духовность" >> "$LOG"
fi
if [ -e 'Психология/Чертоги_разума.txt' ]; then
  echo "SKIP(exists): Чертоги_разума.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Чертоги_разума.txt' 'Психология/Чертоги_разума.txt' && echo "MOVED: Чертоги_разума.txt -> Психология" >> "$LOG" || echo "FAIL: Чертоги_разума.txt -> Психология" >> "$LOG"
fi
if [ -e 'Психология/Шум. Несовершенство человеческих суждений - часть 1.txt' ]; then
  echo "SKIP(exists): Шум. Несовершенство человеческих суждений - часть 1.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Шум. Несовершенство человеческих суждений - часть 1.txt' 'Психология/Шум. Несовершенство человеческих суждений - часть 1.txt' && echo "MOVED: Шум. Несовершенство человеческих суждений - часть 1.txt -> Психология" >> "$LOG" || echo "FAIL: Шум. Несовершенство человеческих суждений - часть 1.txt -> Психология" >> "$LOG"
fi
if [ -e 'Психология/Шум. Несовершенство человеческих суждений - часть 2.txt' ]; then
  echo "SKIP(exists): Шум. Несовершенство человеческих суждений - часть 2.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/Шум. Несовершенство человеческих суждений - часть 2.txt' 'Психология/Шум. Несовершенство человеческих суждений - часть 2.txt' && echo "MOVED: Шум. Несовершенство человеческих суждений - часть 2.txt -> Психология" >> "$LOG" || echo "FAIL: Шум. Несовершенство человеческих суждений - часть 2.txt -> Психология" >> "$LOG"
fi
if [ -e 'Развитие/Эго, или Наделенный собой.txt' ]; then
  echo "SKIP(exists): Эго, или Наделенный собой.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Эго, или Наделенный собой.txt' 'Развитие/Эго, или Наделенный собой.txt' && echo "MOVED: Эго, или Наделенный собой.txt -> Развитие" >> "$LOG" || echo "FAIL: Эго, или Наделенный собой.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Развитие/Этим утром я решила перестать есть_transcription.txt' ]; then
  echo "SKIP(exists): Этим утром я решила перестать есть_transcription.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/Этим утром я решила перестать есть_transcription.txt' 'Развитие/Этим утром я решила перестать есть_transcription.txt' && echo "MOVED: Этим утром я решила перестать есть_transcription.txt -> Развитие" >> "$LOG" || echo "FAIL: Этим утром я решила перестать есть_transcription.txt -> Развитие" >> "$LOG"
fi
if [ -e 'Здоровье/Эффект_теломер_революционный_подход_к_более_молодой,_здоровой_и.txt' ]; then
  echo "SKIP(exists): Эффект_теломер_революционный_подход_к_более_молодой,_здоровой_и.txt -> Здоровье" >> "$LOG"
else
  mv 'свободные_книги/Эффект_теломер_революционный_подход_к_более_молодой,_здоровой_и.txt' 'Здоровье/Эффект_теломер_революционный_подход_к_более_молодой,_здоровой_и.txt' && echo "MOVED: Эффект_теломер_революционный_подход_к_более_молодой,_здоровой_и.txt -> Здоровье" >> "$LOG" || echo "FAIL: Эффект_теломер_революционный_подход_к_более_молодой,_здоровой_и.txt -> Здоровье" >> "$LOG"
fi
if [ -e 'Здоровье/Эффект_теломер_революционный_подход_к_более_молодой,_здоровой_и2.txt' ]; then
  echo "SKIP(exists): Эффект_теломер_революционный_подход_к_более_молодой,_здоровой_и2.txt -> Здоровье" >> "$LOG"
else
  mv 'свободные_книги/Эффект_теломер_революционный_подход_к_более_молодой,_здоровой_и2.txt' 'Здоровье/Эффект_теломер_революционный_подход_к_более_молодой,_здоровой_и2.txt' && echo "MOVED: Эффект_теломер_революционный_подход_к_более_молодой,_здоровой_и2.txt -> Здоровье" >> "$LOG" || echo "FAIL: Эффект_теломер_революционный_подход_к_более_молодой,_здоровой_и2.txt -> Здоровье" >> "$LOG"
fi
if [ -e 'Психология/еда и мозг.txt' ]; then
  echo "SKIP(exists): еда и мозг.txt -> Психология" >> "$LOG"
else
  mv 'свободные_книги/еда и мозг.txt' 'Психология/еда и мозг.txt' && echo "MOVED: еда и мозг.txt -> Психология" >> "$LOG" || echo "FAIL: еда и мозг.txt -> Психология" >> "$LOG"
fi
if [ -e 'Финансы/путь к финансовой независимости.txt' ]; then
  echo "SKIP(exists): путь к финансовой независимости.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/путь к финансовой независимости.txt' 'Финансы/путь к финансовой независимости.txt' && echo "MOVED: путь к финансовой независимости.txt -> Финансы" >> "$LOG" || echo "FAIL: путь к финансовой независимости.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Финансы/путь к финансовой свободен.txt' ]; then
  echo "SKIP(exists): путь к финансовой свободен.txt -> Финансы" >> "$LOG"
else
  mv 'свободные_книги/путь к финансовой свободен.txt' 'Финансы/путь к финансовой свободен.txt' && echo "MOVED: путь к финансовой свободен.txt -> Финансы" >> "$LOG" || echo "FAIL: путь к финансовой свободен.txt -> Финансы" >> "$LOG"
fi
if [ -e 'Развитие/сначала скажите нет.txt' ]; then
  echo "SKIP(exists): сначала скажите нет.txt -> Развитие" >> "$LOG"
else
  mv 'свободные_книги/сначала скажите нет.txt' 'Развитие/сначала скажите нет.txt' && echo "MOVED: сначала скажите нет.txt -> Развитие" >> "$LOG" || echo "FAIL: сначала скажите нет.txt -> Развитие" >> "$LOG"
fi
