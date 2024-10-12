;; Practice A
(print "Output of A in Static binding = 40")
(print "Output of A in Dynamic binding = 20")


;; Practice B
(print "Output of B in Static binding = 401")
(print "Output of B in Dynamic binding = 5")


;; Practice C
(print "Output of C in Static binding = 9")
(print "Output of C in Dynamic binding = 2")

;; Please write your converted Emacs Lisp code below.
(let ((a 9) (b 1))
    (let ((printa (lambda () (print a))))
      (let ((foo (lambda (b)
                   (let ((a b))
                     (funcall printa)))))
        (funcall foo 2))))


