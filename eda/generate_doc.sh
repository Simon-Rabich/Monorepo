# shellcheck disable=SC2044
for f in $(find event_driven_architecture/docs/source -name '*.yml');
	do file=$(echo "$f" | sed 's/.yml//;s/docs//;s/source//'); ag --force-write "$f" @asyncapi/html-template -o ./docs/generated/"$file"/;
done
