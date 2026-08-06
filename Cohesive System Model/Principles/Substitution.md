---
realm: Principles
kind: principle
created: 2026-08-06
updated: 2026-08-06
status: draft
aliases:
  - Substitution Lemma
  - Capture-Avoiding Substitution
  - Reindexing by Substitution
---

# Substitution

Substitution replaces variables with terms while preserving the binding, scope, sorting, typing, and contextual relationships that make an expression meaningful. It is a foundational operation in [[Logic|logic]], [[Type Theory|type theory]], the [[Lambda Calculus|lambda calculus]], rewriting, proof theory, and compiler semantics.

The notation

$$
t[s/x]
$$

denotes the result of replacing the free occurrences of variable $x$ in term $t$ by term $s$. Bound occurrences of $x$ are not replaced, and variables free in $s$ must not become accidentally bound by binders surrounding the replacement sites.

## Binding and Capture Avoidance

Substitution is defined relative to free and bound variables. For example, naively substituting $y$ for $x$ in $\lambda y.x$ would produce $\lambda y.y$ and incorrectly capture the formerly free $y$. Capture-avoiding substitution first renames the binder to a fresh variable:

$$
(\lambda y.x)[y/x]
\equiv_{\alpha}
(\lambda z.x)[y/x]
=
\lambda z.y.
$$

Alpha-equivalent expressions differ only by consistent renaming of bound variables. A correct substitution operation must respect alpha-equivalence, freshness, shadowing, and the binding rules of every syntactic form. De Bruijn indices, locally nameless representations, nominal techniques, higher-order abstract syntax, and explicit-substitution calculi are alternative realizations of this discipline.

## Substitution Lemma

The substitution lemma states that well-formed substitution preserves the relevant judgement. In a dependent typing form, if

$$
\Gamma,x:A,\Delta \vdash t:T
\qquad\text{and}\qquad
\Gamma \vdash a:A,
$$

then, subject to the theory's side conditions,

$$
\Gamma,\Delta[a/x] \vdash t[a/x] : T[a/x].
$$

In a simply typed calculus, later context and result types may not depend on $x$, so the corresponding statement is simpler. In logic, substitution preserves well-formed formulas and derivations under admissible replacement. In operational semantics, substitution lemmas commonly support preservation or subject-reduction proofs.

Nested substitutions must also commute according to their dependencies. In simultaneous form, substitutions behave like identity and composition:

$$
t[\mathrm{id}] = t,
\qquad
t[\tau][\sigma] = t[\tau\circ\sigma].
$$

The orientation reflects that expressions are reindexed contravariantly: a context substitution $\sigma:\Gamma\to\Delta$ assigns terms in context $\Gamma$ to the variables declared by $\Delta$, and turns an expression over $\Delta$ into one over $\Gamma$.

Paul Taylor emphasizes that the substitution lemma is the commuting law for successive substitutions. When the expression being acted upon is omitted, this law becomes composition of abstract morphisms in the category of contexts and substitutions. Associativity is therefore not incidental bookkeeping; it is the categorical coherence of substitution.

## Substitution of Terms Is Composition

Suppose a term $t(x)$ denotes a function $t:A\to B$ and a term $s(y)$ denotes $s:B\to C$. Substituting $t(x)$ for $y$ in $s(y)$ yields:

$$
s(t(x))
$$

whose denotation is ordinary composition:

$$
A \xrightarrow{t} B \xrightarrow{s} C,
\qquad
\left[\!\left[s[t/y]\right]\!\right]
=
\left[\!\left[s\right]\!\right]\circ
\left[\!\left[t\right]\!\right].
$$

Contexts form the objects of a syntactic or classifying category, while simultaneous substitutions form its morphisms. Identity substitutions supply identity morphisms and the substitution lemma supplies associative composition. This is the precise sense in which substitution of terms is composition.

## Substitution as Pullback

Substitution into a predicate or dependent type has another categorical form. Let $t:A\to B$ be a term and let a predicate $P$ on $B$ be represented by a subobject $i:P\hookrightarrow B$. Substituting $t(x)$ into $P(y)$ produces the predicate

$$
Q(x) \equiv P(t(x)).
$$

Its extension is the inverse image:

$$
Q = \{x\in A \mid t(x)\in P\}
  \cong A\times_B P.
$$

The square

$$
\begin{array}{ccc}
Q = A\times_B P & \xrightarrow{\;\pi_P\;} & P \\
{\scriptstyle \pi_A}\big\downarrow & & \big\downarrow{\scriptstyle i} \\
A & \xrightarrow{\;t\;} & B
\end{array}
\qquad
t\circ\pi_A = i\circ\pi_P
$$

is a pullback. The pullback reindexes the predicate from $B$ to $A$ while retaining exactly the witnesses lying over points selected by $t$.

For a dependent type represented by a display map $p:E\to B$, substitution along $t:A\to B$ similarly produces the pullback family:

$$
t^{*}E = A\times_B E \longrightarrow A.
$$

In an indexed or fibrational presentation, substitution is the reindexing functor $t^*$ between fibers. Functoriality gives:

$$
\mathrm{id}^{*}\cong\mathrm{Id},
\qquad
(s\circ t)^{*}\cong t^{*}\circ s^{*},
$$

with strict equality or coherent isomorphism depending on the chosen semantic structure.

The slogan “substitution is pullback” must retain its boundary. As Taylor notes, syntactic substitution is not necessarily implemented by first constructing an arbitrary pullback in the syntactic category. One defines the original and substituted expressions and then proves that their denotations satisfy the relevant pullback universal property. A syntactic category need not possess every pullback merely because these substitution squares are pullbacks.

Predicate substitution can also appear as composition when a predicate is represented by a characteristic map $P:B\to\Omega$: the substituted predicate is $P\circ t:A\to\Omega$. This is compatible with the pullback account because inverse images of classified subobjects are obtained by composing characteristic maps.

## Lambda Calculus and Functional Programming

In the [[Lambda Calculus|lambda calculus]], beta reduction is defined by substitution:

$$
(\lambda x.t)\,u \longrightarrow_{\beta} t[u/x].
$$

The rule explains function application at the syntactic level, while alpha-renaming ensures that the replacement is capture avoiding. Substitution also underlies proofs of confluence, preservation, normalization, and equivalence.

[[Functional Programming|Functional programming]] languages need not realize application by physically copying syntax. Closures pair code with an environment; interpreters may extend environments; compilers may use lexical addresses, SSA values, inlining, specialization, or graph reduction. These mechanisms realize the semantic effect of substitution while preserving sharing, evaluation strategy, effects, and cost behavior.

Substitution can duplicate a term syntactically even when evaluation shares its result, or substitute a term into a position that is never evaluated. Call-by-name, call-by-value, and call-by-need therefore agree on selected denotational equations while differing operationally.

## Logic, Processes, and Realization

In quantified logic, substitution instantiates variables in terms and formulas subject to freedom-for-substitution conditions. In [[Process Calculi|process calculi]], communication can substitute a transmitted name for an input-bound variable. In relational and logic programming, an answer substitution assigns terms to query variables, while unification constructs substitutions that make expressions agree.

A compiler-like [[Realization|realization]] should distinguish:

- Syntactic substitution in an authored or canonical language.
- Semantic reindexing across contexts, predicates, or dependent types.
- Environment lookup, closure capture, inlining, specialization, or name passing as execution mechanisms.
- Replacement of one system role or substrate mechanism by another, which is a realization change and not automatically formal substitution.

Correct lowering must preserve binding, type and proof judgements, identity, sharing, effects, evaluation order, and the relevant notion of equality. Text replacement is not an adequate substitute for a scoped substitution operation.

## Modeling Checks

- Which occurrences are free, which are bound, and how is freshness represented?
- Is substitution capture avoiding and stable under alpha-equivalence?
- Does the substitution lemma preserve typing, derivability, equality, or another judgement?
- Is the operation term-into-term composition or predicate/type reindexing by pullback?
- What are the source and target contexts of a simultaneous substitution?
- Is functoriality strict or only coherent up to isomorphism?
- Does the implementation copy syntax, extend an environment, preserve sharing, or communicate a name?
- Which effects or evaluation choices make two substitution realizations observably different?

## External References

- Andrej Bauer, [Substitution is pullback](https://math.andrej.com/2012/09/28/substitution-is-pullback/), including Paul Taylor's comments on the substitution lemma and the category of contexts and substitutions, 2012.

Related concepts: [[Lambda Calculus|lambda calculus]], [[Functional Programming|functional programming]], [[Logic|logic]], [[Type Theory|type theory]], [[Judgement|judgement]], [[Curry–Howard Correspondence|Curry–Howard correspondence]], [[Process Calculi|process calculi]], [[Relational and Logic Programming|relational and logic programming]], [[Reduction, Evaluation, and Confluence|reduction, evaluation, and confluence]], [[Fibrations and Indexed Structure|fibrations and indexed structure]], [[Universal Constructions|universal constructions]], [[Functoriality|functoriality]], [[Naturality|naturality]], [[Boundaries|boundaries]], [[Realization|realization]].

## Formal relations

- `constrains`: [[Lambda Calculus]] — Requires beta reduction and related term transformations to preserve binding, freshness, alpha-equivalence, and well-formed judgements.
- `corresponds_to`: [[Universal Constructions]] — Predicate and dependent-type substitution is modeled by pullback along the substituted term, while term substitution retains its separate composition account.
