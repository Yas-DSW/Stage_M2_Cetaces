 rule hello:
     output:'output.txt'
     shell:'echo "Hello world">{output}'

 rule World :
         input : 'output.txt'
         output : 'hello.txt'
         shell :
         'cat {input} > {output} | echo "Cette nouvelle ligne vient d\'être ajouter" >> {output}'

