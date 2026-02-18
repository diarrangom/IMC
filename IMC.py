import streamlit as st

st.title("Indice de Masse Corporelle")

st.write("L'indice de Masse Corporelle (IMC) est bien plus qu'un simple chiffre : c'est l'outil de référence internationale pour évaluer la corpulence d'une personne adulte. Inventé au XIXe siécle par le mathématicien belge ADdolphe Quetelet, il es aujourd'hui validé par l'Organisation Mondiale de la Santé (OMS) pour identifier les risques liés au poids")

st.markdown("___")

st.header("Déterminer mon IMC")

poids=st.number_input("Veuillez entrer votre poids (kg)")
taille=st.number_input("Veuillez entrer votre taille (m)")

if st.button("Calculer mon IMC"):
    if taille<=0.5:
        st.warning("🛑 Cette taille semble correspondre à un nourrisson. L'IMC standard ne s'applique pas de la meme maniére")
        
    if taille>0:
        imc= poids/(taille**2)
        st.write(imc)

        if poids<=2 :
            st.warning("🛑 Le poids est trop faible pour un calcul d'IMC")

        elif taille>2.51:
            st.warning("🛑 Valeur Impossible. La taille saisi dépasse le record du monde enregistré (2.51m). Veuillez vérifier votre saisie")
            
        elif imc<18.5:
            st.warning("Catégorie : Maigre")
            st.markdown("___")
            st.header("Conseils")
            st.write("""
            - Alimentation : Augmentez l'apport calorique avec des aliments denses (noix, avocats, huiles végétales).
            - Activité : Privilégiez le renforcement musculaire (musculation douce) pour gagner de la masse saine plutot que de faire trop de cardio.
            - Santé : Assurez-vous d'avoir un apport suffisant en protéines et vitamines.""")
            
        elif 18.5<=imc<25:
            st.success("Catégorie : Normal")
            st.markdown("___")
            st.header("Conseils")
            st.write("""
            - Alimentation : Continuez à manger varié et équilibré sans restrictions inutiles.
            - Activité : Variez les plaisirs ! Un mélange de cardio (course, vélo) et de souplesse (yoga, étirements) est idéal.
            - Santé : L'objectif est la stabilisation et le maintien de votre énergie.""")
            
        elif 25<=imc<30:
            st.warning("Catégorie : Surpoids")
            st.markdown("___")
            st.header("Conseils")
            st.write("""
            - Alimentation : Réduisez les sucres rapides et les produits transformés. Priviligiez les fibres (légumes, céréales complétes).
            - Activité : Visez au moins 30 minutes de marche rapide ou d'activité modérée par jour.
            - Santé : Ne cherchez pas un régime drastique, mais de petites habitudes durables.""")

        elif imc>=30:
            st.warning("Catégorie : Obése")
            st.markdown("___")
            st.header("Conseils")
            st.write("""
            - Alimentation : Il est conseillé de consulter un nutritionniste pour un plan adapté sans carences.
            - Activité : Privilégiez les activités "portées" pour protéger vos articulations (natation, aquagym, vélo).
            - Santé : Un suivi médical est recommandé pour surveillez la tension et le taux de sucre.""")
        
        elif poids> 300:
            st.warning("🛑 Attention ! L'IMC n'est plus un indicateur fiable pour des poids supérieurs à 300kg. Consultez un spécialiste.")
        
        elif poids>635:
            st.warning("🛑 Valeur Impossible. Le poids saisi dépasse le record mondial enregistré (635 kg). Veuillez vérifier votre saisie")

    else:
        st.info("🛑 La taille ne peux pas etre égale à 0. Le calcul est impossible.")

st.markdown("___")

st.header("Votre zone d'équilibre")
st.write("L'IMC est un indicateur, mais votre bien-être est un objectif concret. Cette section vous aide à visualiser votre poids de forme : celui qui protège votre cœur, préserve vos articulations et booste votre énergie quotidienne. Plutôt que de viser un chiffre fixe, découvrez l'intervalle de poids qui correspond à votre morphologie pour une santé durable.")
poids_min = 18.5*(taille**2)
poids_max = 25*(taille**2)
if st.button("Determiner mon poids idéal"):
    st.write("Pour votre taille de",taille, "m, cette zone se situe entre,",poids_min, "kg et,", poids_max, "kg.")
    
st.markdown("___")

st.header("Classification")
st.image("IMC.jpg")

st.markdown("___")

st.header("Importance de connaitre son IMC")
st.write("""
**Identifier les risques pour la santé**

Le véritable intérêt n'est pas esthétique, il est médical. Un IMC en dehors de la zone de "normalité" est souvent corrélé à une augmentation statistique des risques de :
- Maladie cardiovasculaire
- Accident vasculaire cérébral
- Hypertension artérielle
- Infertilité
- Dépression et anxiété
- Maladie du foie gras non alcoolique (NAFLD)/stéatohépatite non alcoolique (NASH)
- Apnée obstructive du sommeil et problèmes respiratoires
- Maladie rénale chronique
- Divers types de cancer : notamment les cancers du sein, du côlon, de l'endomètre, de l'œsophage, du rein, de l'ovaire et du pancréas
- Arthrose du genou
- Maladie des calculs biliaires
- Thrombose

**Un langage commun avec les professionnels**

L'IMC est une mesure universelle. Que vous voyiez un médecin à Dakar, New York ou Paris, ce chiffre permet de suivre l'évolution de votre santé sur le long terme de manière objective.
""")

st.markdown("___")

st.header("Les limites de l'IMC")
st.write("""
L'IMC est un outil précieux mais imparfait. Il ne faut pas le prendre comme une vérité absolue car il ne fait pas la différence entre :
- Le muscle et la graisse : Un athlète très musclé peut avoir un IMC "obèse" alors qu'il a très peu de masse grasse.
- La répartition des graisses : La graisse abdominale (autour du ventre) est beaucoup plus dangereuse pour le cœur que la graisse stockée ailleurs, ce que l'IMC ne précise pas.""")

