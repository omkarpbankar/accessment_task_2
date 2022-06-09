import streamlit as st
import mysql.connector as connection


def main():

	st.header("Streamlit App for Banking by Omkar.")
	
	operations = ["Check Balance","Withdraw", "Account Statement"]

	choice =st.sidebar.selectbox("Choose your option", operations)
	
	if choice == 'Check Balance':
		st.subheader("Kindly enter user id to check the balance")
		user_id=st.input("Please enter your user id")
		pass
	elif choice == 'Withdraw':
		pass
	elif choice == 'Account Statement':
		pass




if __name__ == '__main__':
	main()