while IFS= read -r line; do
 	whois "$line" >> whois.txt
done < all.txt