# Example aliases
alias saws='aws-env -e staging > ~/.kaws/$$.currenv ; source ~/.kaws/$$.currenv ; rm ~/.kaws/$$.currenv ; echo "${AWS_ACCOUNT}"'
alias paws='aws-env -e production > ~/.kaws/$$.currenv ; source ~/.kaws/$$.currenv ; rm ~/.kaws/$$.currenv ; echo "${AWS_ACCOUNT}"'
