
alias saws='aws-env -e staging > ~/.k.aws/$$.currenv ; source ~/.k.aws/$$.currenv ; rm ~/.k.aws/$$.currenv ; echo "${AWS_ACCOUNT}"'
alias paws='aws-env -e production > ~/.k.aws/$$.currenv ; source ~/.k.aws/$$.currenv ; rm ~/.k.aws/$$.currenv ; echo "${AWS_ACCOUNT}"'
alias uaws='aws-env -e utility > ~/.k.aws/$$.currenv ; source ~/.k.aws/$$.currenv ; rm ~/.k.aws/$$.currenv ; echo "${AWS_ACCOUNT}"'
alias uataws='aws-env -e uat > ~/.k.aws/$$.currenv ; source ~/.k.aws/$$.currenv ; rm ~/.k.aws/$$.currenv ; echo "${AWS_ACCOUNT}"'
alias aaws='aws-env -e analytics > ~/.k.aws/$$.currenv ; source ~/.k.aws/$$.currenv ; rm ~/.k.aws/$$.currenv ; echo "${AWS_ACCOUNT}"'
alias tpsaws='aws-env -e testprep-staging > ~/.k.aws/$$.currenv ; source ~/.k.aws/$$.currenv ; rm ~/.k.aws/$$.currenv ; echo "${AWS_ACCOUNT}"'
alias tppaws='aws-env -e testprep-production > ~/.k.aws/$$.currenv ; source ~/.k.aws/$$.currenv ; rm ~/.k.aws/$$.currenv ; echo "${AWS_ACCOUNT}"'
alias rsaws='aws-env -e readiness-staging > ~/.k.aws/$$.currenv ; source ~/.k.aws/$$.currenv ; rm ~/.k.aws/$$.currenv ; echo "${AWS_ACCOUNT}"'
alias rpaws='aws-env -e readiness-production > ~/.k.aws/$$.currenv ; source ~/.k.aws/$$.currenv ; rm ~/.k.aws/$$.currenv ; echo "${AWS_ACCOUNT}"'