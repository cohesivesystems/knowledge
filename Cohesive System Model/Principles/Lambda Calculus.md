---
realm: Principles
kind: discipline
created: 2026-08-06
updated: 2026-08-06
status: draft
aliases:
  - Lambda Calculi
  - λ-Calculus
  - λ-Calculi
---

# Lambda Calculus

The lambda calculus is a formal calculus of variables, function abstraction, application, and [[Substitution|substitution]]. It supplies a foundational language for functions and evaluation, and underlies large parts of [[Functional Programming|functional programming]], [[Type Theory|type theory]], proof theory, and categorical semantics.

The untyped core has the grammar:

$$
t,u ::= x \mid \lambda x.t \mid t\,u.
$$

A variable $x$ refers to an assumption or binding in scope. An abstraction $\lambda x.t$ binds $x$ in body $t$. An application $t\,u$ applies the function-denoting term $t$ to argument $u$.

## Binding and Conversion

Three central relations organize lambda terms:

- **Alpha conversion** renames bound variables consistently: $\lambda x.t \equiv_{\alpha} \lambda y.t[y/x]$ when $y$ is fresh.
- **Beta reduction** applies an abstraction by capture-avoiding substitution: $(\lambda x.t)u \to_{\beta} t[u/x]$.
- **Eta conversion** expresses function extensionality at the syntactic level: $\lambda x.f x \equiv_{\eta} f$ when $x$ is not free in $f$.

Alpha conversion is not computation; it records that binder names are inessential. Beta reduction is the core computation rule. Eta conversion identifies a function with an abstraction that merely forwards its argument, but whether eta is definitional equality, propositional equality, or an optimization law depends on the calculus.

Capture avoidance is essential. A substitution that turns a free variable into a bound variable changes meaning. Concrete implementations use names and freshness, De Bruijn indices, locally nameless representations, nominal syntax, closures, or higher-order abstract syntax to preserve binding correctly.

## Untyped and Typed Calculi

The untyped lambda calculus permits self-application and can express general recursive computation. Fixed-point combinators such as $Y$ satisfy:

$$
YF = F(YF)
$$

under the calculus's conversion theory, allowing recursive behavior without naming the recursive function. Untyped terms may diverge and need not have normal forms.

The simply typed lambda calculus assigns function types and excludes many ill-formed applications. Its core typing rules support judgements such as:

$$
\Gamma \vdash t:A.
$$

The simply typed calculus is strongly normalizing and cannot express unrestricted general recursion without an extension. Products, sums, unit and empty types, polymorphism, dependent types, recursive types, effects, modalities, and [[Linear Logic|linear or affine types]] yield different typed lambda calculi with different expressive and normalization properties.

“The lambda calculus” should therefore be qualified when a theorem depends on typing, evaluation strategy, extensionality, recursion, effects, or particular constants.

## Reduction and Evaluation

Pure beta reduction is confluent: if a term reduces along two paths, the paths can be joined. A normal form is therefore unique when it exists, up to the chosen conversion theory. Confluence does not imply that every term terminates or that every evaluation strategy reaches an existing normal form.

Common evaluation disciplines include normal order, applicative order, call-by-name, call-by-value, and call-by-need. They choose which beta redex is evaluated and when argument work is performed or shared. With effects or divergence, these choices can change observable behavior.

[[Reduction, Evaluation, and Confluence|Reduction, evaluation, and confluence]] records the distinction between the full conversion relation and an operational strategy. A programming language may use lambda syntax while specifying only selected evaluation contexts and treating other beta equations as invalid in the presence of effects.

## Substitution and Composition

Beta reduction presents application through syntactic substitution, but the semantic structure is compositional. If terms denote morphisms, substituting one term into another denotes composition. Simultaneous substitutions form morphisms between contexts and obey identity and associativity through the substitution lemma.

For predicates and dependent types, [[Substitution|substitution as pullback]] reindexes a family along a term. This separates two related claims:

- Substitution of terms into terms is composition.
- Substitution into predicates or dependent types is inverse-image reindexing, modeled by pullback.

Both are needed in categorical semantics of dependent lambda calculi.

## Curry–Howard and Logic

Under the [[Curry–Howard Correspondence|Curry–Howard correspondence]], typed lambda terms are proof terms. Function types correspond to implication, abstraction to implication introduction, application to elimination, and beta normalization to proof normalization.

Different calculi correspond to different logics. Simply typed lambda calculus aligns with intuitionistic propositional logic; System F supports a second-order constructive interpretation; dependent lambda calculi support quantified propositions; linear lambda calculi reflect [[Linear Logic|linear logic]]. Classical principles such as the [[Law of Excluded Middle|law of excluded middle]] require axioms, translations, continuations, control operators, or another explicit computational interpretation rather than appearing unchanged in the ordinary constructive calculus.

## Categorical Semantics

Cartesian closed categories model simply typed lambda calculus with products and function types. Contexts are interpreted by products, terms by morphisms, application by evaluation, and abstraction by currying. Beta and eta laws correspond to the equations governing the exponential adjunction.

In this view:

- A judgement $x:A\vdash t:B$ denotes a morphism $A\to B$.
- A closed term $\vdash t:A$ denotes a morphism $1\to A$.
- Substitution of terms denotes morphism composition.
- Renaming and weakening arise from context morphisms and cartesian structure.

Linear lambda calculi replace cartesian structure with symmetric monoidal closed structure. Dependent type theories require indexed, fibrational, comprehension, or locally cartesian closed structure in which types vary over contexts and substitution reindexes them.

## Process Calculi and Concurrency

[[Process Calculi|Process calculi]] broaden the primary computational picture from evaluation of one term to interaction among concurrent processes. Encodings such as Milner's *Functions as Processes* represent lambda abstractions and applications by π-calculus processes and communication protocols.

This is a qualified generalization, not a claim that every process calculus contains every lambda calculus unchanged. An encoding must state which evaluation strategy, observations, and equivalence it preserves. Conversely, lambda calculi can host concurrency through effects, channels, continuations, monads, or process-valued terms without making interaction identical to beta reduction.

## Functional Programming and Realization

Functional languages inherit abstraction, application, lexical scope, higher-order functions, and equational reasoning from lambda calculi. Real languages also add data types, modules, pattern matching, recursion, effects, exceptions, concurrency, resource management, and operational cost models.

A compiler rarely realizes beta reduction by repeatedly copying source syntax. Closures, environments, stack frames, registers, graph reduction, inlining, specialization, continuation passing, and machine code can all realize application. A correct compiler preserves the selected observational semantics rather than the surface reduction steps themselves.

The lambda calculus is therefore a semantic and proof-theoretic foundation, not a claim that a production runtime is a literal term-rewriting engine. Compiler-like [[Realization|realization]] must name which equalities, evaluation order, sharing, effects, termination, and resource behavior survive lowering.

## Modeling Checks

- Is the calculus typed or untyped, and which term and type constructors exist?
- Which variables are free or bound, and how is alpha-equivalence represented?
- Is substitution capture avoiding?
- Which reductions are definitional, and which evaluation strategy is operational?
- Does the calculus normalize, permit divergence, or include a fixed-point operator?
- Which effects make beta or eta equations observable or invalid?
- What logic and categorical structure correspond to the calculus?
- Which observations must an encoding or compiler preserve?

## External References

- Alonzo Church, [An Unsolvable Problem of Elementary Number Theory](https://doi.org/10.2307/2268571), *American Journal of Mathematics* 58(2):345-363, 1936.
- Gordon D. Plotkin, [Call-by-Name, Call-by-Value and the Lambda-Calculus](https://doi.org/10.1016/0304-3975(75)90017-1), *Theoretical Computer Science* 1(2):125-159, 1975.
- Robin Milner, [Functions as Processes](https://doi.org/10.1017/S0960129500001407), *Mathematical Structures in Computer Science* 2(2):119-141, 1992.

Related concepts: [[Substitution|substitution]], [[Functional Programming|functional programming]], [[Type Theory|type theory]], [[Logic|logic]], [[Judgement|judgement]], [[Curry–Howard Correspondence|Curry–Howard correspondence]], [[Linear Logic|linear logic]], [[Law of Excluded Middle|law of excluded middle]], [[Reduction, Evaluation, and Confluence|reduction, evaluation, and confluence]], [[Recursion|recursion]], [[Fixed Points|fixed points]], [[Process Calculi|process calculi]], [[Categorical Principles|categorical principles]], [[Fibrations and Indexed Structure|fibrations and indexed structure]], [[Functoriality|functoriality]], [[Compositionality|compositionality]], [[Realization|realization]].

## Formal relations

- `corresponds_to`: [[Functional Programming]] — Relates functional abstraction, application, lexical binding, substitution, and evaluation to a foundational term calculus without identifying every functional language with one lambda calculus.
