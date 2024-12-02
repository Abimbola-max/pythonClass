 menuAnswer = int(input("Nokia Menu Functions, Please Press:\n1. Phone Book\n2. To enter Messages\n3. To enter Chat\n4. To enter call register\n5. Tones\n6. Settings\n7. Call divert\n8. Games\n9. Calculator\n10 Reminders\n11. Clock\n12. SIM services\nEnter an option: "))

	
match (menuAnswer):
	case 1: 
		taskAnswer= int(input("Select one:\n1. Search\n2. Service Nos.\n3. Add name\n4. Erase\n5. Edit\n6 Assign tone\n7. Send b'card\n8. Options\n9. Speed dials\n10. Voice tags\nEnter an option: "))

	match (taskAnswer):
		case 1:print("Search....");
		       
		case 2: print("Service Nos......");
			
		case 3:print("Add your name.....");
			
		case 4:print("Erase.....");
			
		case 5:print("Edit.....");
			
		case 6: print("Assign tone.....");
			
		case 7: print("Send b'card.....");
			
		case 8:
			optionAnswer = int(input("Select One:\n1. Type of view\n2. Memory status\n"))
		match (optionAnswer):
		case 1:print("The Type of view");
			
		case 2:print("Memory Status");}
			

		case 9:print("Speed dials.....");
			
		case 10:print("Voice tags");}
			


		case 2: messageAnswer = int(input("Messages, Select one:\n1. Write messages\n2. Inbox\n3. Outbox\n4. Picture Messages\n5. Templates\n6 Smileys\n7. Message setings\n8. Info service\n9. Voice mailbox number\n10. Service command editor\nEnter an option; "))
	
	match(messageAnswer):
		case 1: print("Type your messages:......");
			
		case 2: print("Your inbox:......");
			
		case 3: print("Your Outbox:......");
			
		case 4: print("Your picture messages:......");
			
		case 5: print("Your Templates:......");
			
		case 6: print("Your Smileys:......");
			
		case 7: messageSettingsAnswer = int(input("Choose One:\n1. Set 1\n2.Common\n>>>"))

	match(messageSettingsAnswer):
		case 1: set1Answer = int(input("SET 1,  Choose one:\n1. Message centre number\n2. Messages sent as\n3. Message validity\nEnter an option: "))

	match(set1Answer):
		case 1: print("Your Message centre number:......");
			
		case 2: print("Messages sent as:......");
			
		case 3: print("Message validity:......");}
			
		case 2: commonAnswer = int(input("COMMON Settings,  Choose one:\n1. Delivery reports\n2. Reply via same centre\n3. Character support\nEnter an option: "))
	
	match(commonAnswer):
		case 1: print("Delivery reports:......")
			
		case 2: print("Reply via same centre:......")
			
		case 3: print("Character support:......")

		case 8: print("Info service:......")
			
		case 9: print("Voice mailbox number:......")
			
		case 10: print("Service command editor:......")
			
		
		case 3: print("Your chat.......")
			


		case 4: callRegisterAnswer = int(input("Call Register, Choose One:\n1. Missed calls\n2. Received calls\n3. Dialled number\n4. Erase recent call lists\n5. Show call duration\n6. Show call costs\n7. Call cost settings\n8. Prepaid credit\nEnter an option: "))

	
	match (callRegisterAnswer):
		case 1: print("Your Missed calls.....");
			break;
		case 2: print("Your Received calls....");
			break;
		case 3: print("Your Dialled numbers....")
			break;
		case 4: print("Erase recent call lists....")
			break;
		case 5: callDurationAnswer = int(input("Call duration, Choose One:\n1. Last call duration\n2. All calls' duration\n3. Received calls' duration\n4. Dialled calls' duration\n5. Clear timers\nEnter an option: "))
	
	match (callDurationAnswer):
		case 1: print("Last call duration.....")
			
		case 2: print("All calls' duration.....")
			
		case 3: print("Received calls' duration.....")
			
		case 4: print("Dialled calls' duration.....")
			
		case 5: print("Clear timers.....")
			
		
		case 6: callCostAnswer = int(input("Call costs, Choose One:\n1.Last call cost\n2. All calls' cost\n3. Clear counters\nEnter an option: "))
	
	match (callCostAnswer):
		case 1: print("Last call cost.....")
			
		case 2: print("All calls' cost.....")
			
		case 3: print("Clear counters.....")
			

		case 7: costSettingsAnswer = int(input("Call cost settings, Choose One:\n1.Call cost limit\n2. Show costs in\nEnter an option: "))
	
	match (costSettingsAnswer):
		case 1: print("Call cost limit....")
			
		case 2: print("Show costs in.....")
			
		
		case 8: print("Prepaid credit.....")
			


		case 5:  tonesAnswer = int(input("Tones, Choose One:\n1. Ringing tone\n2. Ringing volume\n3. Incoming call alert\n4. Composer\n5. Message alert tone\n6. Keypad tones\n7. Warning and game tones\n8. Vibrating alert\n9. Screen saver\nEnter an option: "))

		match (tonesAnswer):
		case 1: print("Ringing tone....")
			 
		case 2: print("Ringing Volume....")
			
		case 3: print("Incoming call alert....")
			
		case 4: print("Composer....")
			
		case 5: print("Message alert tone....")
			
		case 6: print("Keypad tones....")
			
		case 7: print("Warning and game tones....")
			
		case 8: print("Vibrating alert....")
			
		case 9: print("Screen saver....")
			
		case 6: settingsAnswer = int(input("Settings, ChooseOne:\n1. Call settings\n2. Phone Settings\n3. Security settings\nEnter an option: "))
	
	match (settingsAnswer):
		case 1: callSettingsAnswer = int(input("Call settings,  Choose One\n1. Automatic redial\n2. Speed dialling\n3. Call waiting options\n4. Own number sending\n5. Phone line in use\n6. Automatic answer\nEnter an option:  "))
	
	match (callSettingsAnswer):
		case 1: print("Automatic redial....")
			
		case 2: print("Speed dialing....")
			
		case 3: print("Call Waiting Options....")
			
		case 4: print("Own number sending.....")
			
		case 5: print("Phone line in use......")
			
		case 6: print("Automatic answer....")
			
		
	 	case 2: phoneSettingsAnswer = int(input("Phone settings,  Choose One\n1. Language\n2. Cell info display\n3. Welcome note\n4. Network selection\n5. Lights\n6. Confirm SIM service action\nEnter an option: "))
	
	match (phoneSettingsAnswer):
		case 1: print("Choose your language......")
			
		case 2: print("Cell info display......")

		case 3: print("Welcome note......")
		
		case 4: print("Network selection......")
			
		case 5: print("Lights......")
			
		case 6: print("Confirm SIM service action......")
			
	
		case 3: securitySettingsAnswer = int(input("Security settings,  Choose One\n1. Pin code Request\n2. Call barring service\n3. Fixed dialling\n4. Closed user group\n5. Phone security\n6. Change access codes\nEnter an option: "))
	
	match (securitySettingsAnswer):
		case 1:	print("PIN code request......")
			
		case 2:	print("Call barring service......")
			
		case 3:	print("Fixed dialling......")
			
		case 4: print("Closed user group......")
			
		case 5: print("Phone security......")
			
		case 6:	print("Change access codes......")
			

		case 4: print("Restore factory settings......")
			
		case 7: print("Call divert.......")
			
		
		case 8: print("Games.......")
			
		case 9: print("Calculator.......")
			
		case 10: print("Remainders.......")
			
		case 11:
			clockAnswer = int(input("Clock, Enter a number:\n1. Alarm clock\n2. Clock settings\n3. Date settings\n4. Stopwatch\n5. Countdown timer\n6. Auto update of date and time\nEnter an option: "))

		match (clockAnswer):
		case 1: print("Alarm clock.......")
			
		case 2: print("Clock setting.......")
			
		case 3: print("Date setting.......")
			
		case 4: print("Stopwatch.......")
			
		case 5: print("Countdown timer.......")
			
		case 6: print("Auto update of date and time.......")
			

			 
		case 12: print("Profiles.......")
			 
		case 13:print("SIM Serive.......")