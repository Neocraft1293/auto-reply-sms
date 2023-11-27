# Auto Reply SMS Script for Termux

Ce script Python est conçu pour être utilisé avec [Termux](https://termux.com/), un émulateur de terminal pour Android. Il permet d'automatiser l'envoi de réponses automatiques à des messages SMS entrants.

## Prérequis

Avant d'utiliser ce script, assurez-vous d'avoir les éléments suivants installés sur votre appareil Android :

- [Termux](https://termux.com/) installé.
- Python et termux-api installé dans Termux. Vous pouvez l'installer en utilisant la commande :
  ```bash
  pkg install python
  pkg install termux-api
  ```
  Les autorisations nécessaires accordées à Termux via ADB depuis un pc. Vous pouvez utiliser les commandes suivantes :
  ```
  adb shell pm grant com.termux android.permission.SEND_SMS
  adb shell pm grant com.termux android.permission.READ_SMS
  adb shell pm grant com.termux android.permission.READ_CONTACTS
  ```
## Utilisation
  
  Clonez ce dépôt sur votre appareil Android.
  Exécutez le script Python à l'aide de Termux.
  Le script surveillera les nouveaux messages SMS entrants et enverra une réponse automatique à ceux qui correspondent aux critères spécifiés.

## Avertissement
  
  Assurez-vous d'utiliser ce script conformément aux lois et réglementations locales. Respectez la vie privée des autres et n'utilisez pas ce script de manière abusive.

