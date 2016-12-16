# this file was generated using ply-3.9\example\yply\yply.py on https://github.com/msxdev/asmsx-cleanup/blob/master/src/z80gen.y

# %{
# #include <stdio.h>
# #include <stdlib.h>
# #include <string.h>
# #include <time.h>
# #include <math.h>
# 
# #include "asmsx.h"
# #include "warnmsg.h"
# 
# #define YYMALLOC	malloc
# #define YYFREE		free
# %}
tokens =  [
  'OP_OR', 'OP_XOR', 'SHIFT_L', 'SHIFT_R', 'OP_OR_LOG', 'OP_AND_LOG', 'NEGATIVE', 'NEGATION', 'OP_NEG_LOG',
  'OP_EQUAL', 'OP_MINOR_EQUAL', 'OP_MINOR', 'OP_MAJOR', 'OP_MAJOR_EQUAL', 'OP_NON_EQUAL', 'APOSTROPHE', 'TEXT',
  'IDENTIFICATOR', 'LOCAL_IDENTIFICATOR', 'PREPRO_LINE', 'PREPRO_FILE', 'PSEUDO_CALLDOS', 'PSEUDO_CALLBIOS',
  'PSEUDO_MSXDOS', 'PSEUDO_PAGE', 'PSEUDO_BASIC', 'PSEUDO_ROM', 'PSEUDO_MEGAROM', 'PSEUDO_SINCLAIR', 'PSEUDO_BIOS',
  'PSEUDO_ORG', 'PSEUDO_START', 'PSEUDO_END', 'PSEUDO_DB', 'PSEUDO_DW', 'PSEUDO_DS', 'PSEUDO_EQU', 'PSEUDO_ASSIGN',
  'PSEUDO_INCBIN', 'PSEUDO_SKIP', 'PSEUDO_DEBUG', 'PSEUDO_BREAK', 'PSEUDO_PRINT', 'PSEUDO_PRINTTEXT', 'PSEUDO_PRINTHEX',
  'PSEUDO_PRINTFIX', 'PSEUDO_SIZE', 'PSEUDO_BYTE', 'PSEUDO_WORD', 'PSEUDO_RANDOM', 'PSEUDO_PHASE', 'PSEUDO_DEPHASE',
  'PSEUDO_SUBPAGE', 'PSEUDO_SELECT', 'PSEUDO_SEARCH', 'PSEUDO_AT', 'PSEUDO_ZILOG', 'PSEUDO_FILENAME', 'PSEUDO_FIXMUL',
  'PSEUDO_FIXDIV', 'PSEUDO_INT', 'PSEUDO_FIX', 'PSEUDO_SIN', 'PSEUDO_COS', 'PSEUDO_TAN', 'PSEUDO_SQRT', 'PSEUDO_SQR',
  'PSEUDO_PI', 'PSEUDO_ABS', 'PSEUDO_ACOS', 'PSEUDO_ASIN', 'PSEUDO_ATAN', 'PSEUDO_EXP', 'PSEUDO_LOG', 'PSEUDO_LN',
  'PSEUDO_POW', 'PSEUDO_IF', 'PSEUDO_IFDEF', 'PSEUDO_ELSE', 'PSEUDO_ENDIF', 'PSEUDO_CASSETTE', 'MNEMO_LD', 'MNEMO_LD_SP',
  'MNEMO_PUSH', 'MNEMO_POP', 'MNEMO_EX', 'MNEMO_EXX', 'MNEMO_LDI', 'MNEMO_LDIR', 'MNEMO_LDD', 'MNEMO_LDDR', 'MNEMO_CPI',
  'MNEMO_CPIR', 'MNEMO_CPD', 'MNEMO_CPDR', 'MNEMO_ADD', 'MNEMO_ADC', 'MNEMO_SUB', 'MNEMO_SBC', 'MNEMO_AND', 'MNEMO_OR',
  'MNEMO_XOR', 'MNEMO_CP', 'MNEMO_INC', 'MNEMO_DEC', 'MNEMO_DAA', 'MNEMO_CPL', 'MNEMO_NEG', 'MNEMO_CCF', 'MNEMO_SCF',
  'MNEMO_NOP', 'MNEMO_HALT', 'MNEMO_DI', 'MNEMO_EI', 'MNEMO_IM', 'MNEMO_RLCA', 'MNEMO_RLA', 'MNEMO_RRCA', 'MNEMO_RRA',
  'MNEMO_RLC', 'MNEMO_RL', 'MNEMO_RRC', 'MNEMO_RR', 'MNEMO_SLA', 'MNEMO_SLL', 'MNEMO_SRA', 'MNEMO_SRL', 'MNEMO_RLD',
  'MNEMO_RRD', 'MNEMO_BIT', 'MNEMO_SET', 'MNEMO_RES', 'MNEMO_IN', 'MNEMO_INI', 'MNEMO_INIR', 'MNEMO_IND', 'MNEMO_INDR',
  'MNEMO_OUT', 'MNEMO_OUTI', 'MNEMO_OTIR', 'MNEMO_OUTD', 'MNEMO_OTDR', 'MNEMO_JP', 'MNEMO_JR', 'MNEMO_DJNZ', 'MNEMO_CALL',
  'MNEMO_RET', 'MNEMO_RETI', 'MNEMO_RETN', 'MNEMO_RST', 'REGISTER', 'REGISTER_IX', 'REGISTER_IY', 'REGISTER_R', 'REGISTER_I',
  'REGISTER_F', 'REGISTER_AF', 'REGISTER_IND_BC', 'REGISTER_IND_DE', 'REGISTER_IND_HL', 'REGISTER_IND_SP', 'REGISTER_16_IX',
  'REGISTER_16_IY', 'REGISTER_PAR', 'CONDITION', 'NUMBER', 'EOL', 'REAL'
]

precedence = [
  ('left', "'+'", "'-'", 'OP_OR', 'OP_XOR'),
  ('left', 'SHIFT_L', 'SHIFT_R'),
  ('left', "'*'", "'/'", "'%'", "'&'"),
  ('left', 'OP_OR_LOG', 'OP_AND_LOG'),
  ('left', 'NEGATIVE'),
  ('left', 'NEGATION', 'OP_NEG_LOG'),
  ('left', 'OP_EQUAL', 'OP_MINOR_EQUAL', 'OP_MINOR', 'OP_MAJOR', 'OP_MAJOR_EQUAL', 'OP_NON_EQUAL')
]

# -------------- RULES ----------------

def p_entry_1(p):
    '''entry : '''

def p_entry_2(p):
    '''entry : entry line'''

def p_line_1(p):
    '''line : pseudo_instruction EOL'''

def p_line_2(p):
    '''line : mnemo_load8bit EOL'''

def p_line_3(p):
    '''line : mnemo_load16bit EOL'''

def p_line_4(p):
    '''line : mnemo_exchange EOL'''

def p_line_5(p):
    '''line : mnemo_arithm16bit EOL'''

def p_line_6(p):
    '''line : mnemo_arithm8bit EOL'''

def p_line_7(p):
    '''line : mnemo_general EOL'''

def p_line_8(p):
    '''line : mnemo_rotate EOL'''

def p_line_9(p):
    '''line : mnemo_bits EOL'''

def p_line_10(p):
    '''line : mnemo_io EOL'''

def p_line_11(p):
    '''line : mnemo_jump EOL'''

def p_line_12(p):
    '''line : mnemo_call EOL'''

def p_line_13(p):
    '''line : PREPRO_FILE TEXT EOL'''
    # {
    # 		strcpy(source, $2);
    # 	}

def p_line_14(p):
    '''line : PREPRO_LINE value EOL'''
    # {
    # 		lines = $2;
    # 	}

def p_line_15(p):
    '''line : label line'''

def p_line_16(p):
    '''line : label EOL'''

def p_label_1(p):
    '''label : IDENTIFICATOR ':''''
    # {
    # 		register_label(strtok($1, ":"));
    # 	}

def p_label_2(p):
    '''label : LOCAL_IDENTIFICATOR ':''''
    # {
    # 		register_local(strtok($1, ":"));
    # 	}

def p_pseudo_instruction_1(p):
    '''pseudo_instruction : PSEUDO_ORG value'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			PC = $2;
    # 			ePC=PC;
    # 		}
    # 	}

def p_pseudo_instruction_2(p):
    '''pseudo_instruction : PSEUDO_PHASE value'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			ePC=$2;
    # 		}
    # 	}

def p_pseudo_instruction_3(p):
    '''pseudo_instruction : PSEUDO_DEPHASE'''
    # {
    # 		if (conditional[conditional_level])
    # 			{
    # 				ePC=PC;
    # 			}
    # 	}

def p_pseudo_instruction_4(p):
    '''pseudo_instruction : PSEUDO_ROM'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			type_rom();
    # 		}
    # 	}

def p_pseudo_instruction_5(p):
    '''pseudo_instruction : PSEUDO_MEGAROM'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			type_megarom(0);
    # 		}
    # 	}

def p_pseudo_instruction_6(p):
    '''pseudo_instruction : PSEUDO_MEGAROM value'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			type_megarom($2);
    # 		}
    # 	}

def p_pseudo_instruction_7(p):
    '''pseudo_instruction : PSEUDO_BASIC'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			type_basic();
    # 		}
    # 	}

def p_pseudo_instruction_8(p):
    '''pseudo_instruction : PSEUDO_MSXDOS'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			type_msxdos();
    # 		}
    # 	}

def p_pseudo_instruction_9(p):
    '''pseudo_instruction : PSEUDO_SINCLAIR'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			type_sinclair();
    # 		}
    # 	}

def p_pseudo_instruction_10(p):
    '''pseudo_instruction : PSEUDO_BIOS'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			if (!bios)
    # 				msx_bios();
    # 		}
    # 	}

def p_pseudo_instruction_11(p):
    '''pseudo_instruction : PSEUDO_PAGE value'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			subpage = ASMSX_MAX_PATH;
    # 			if ($2 > 3)
    # 			{
    # 				error_message(22, __FILE__, __LINE__);
    # 				exit(22);
    # 			}
    # 			else
    # 			{
    # 				PC = 0x4000 * $2;
    # 				ePC = PC;
    # 			}
    # 		}
    # 	}

def p_pseudo_instruction_12(p):
    '''pseudo_instruction : PSEUDO_SEARCH'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			if ((type != MEGAROM) && (type != ROM))
    # 			{
    # 				error_message(41, __FILE__, __LINE__);
    # 				exit(41);
    # 			}
    # 			locate_32k();
    # 		}
    # 	}

def p_pseudo_instruction_13(p):
    '''pseudo_instruction : PSEUDO_SUBPAGE value PSEUDO_AT value'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			if (type != MEGAROM)
    # 			{
    # 				error_message(40, __FILE__, __LINE__);
    # 				exit(40);
    # 			}
    # 			set_subpage($2, $4);
    # 		}
    # 	}

def p_pseudo_instruction_14(p):
    '''pseudo_instruction : PSEUDO_SELECT value PSEUDO_AT value'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			if (type != MEGAROM)
    # 			{
    # 				error_message(40, __FILE__, __LINE__);
    # 				exit(40);
    # 			}
    # 			select_page_direct($2, $4);
    # 		}
    # 	}

def p_pseudo_instruction_15(p):
    '''pseudo_instruction : PSEUDO_SELECT REGISTER PSEUDO_AT value'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			if (type != MEGAROM)
    # 			{
    # 				error_message(40, __FILE__, __LINE__);
    # 				exit(40);
    # 			}
    # 			select_page_register($2, $4);
    # 		}
    # 	}

def p_pseudo_instruction_16(p):
    '''pseudo_instruction : PSEUDO_START value'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			start=$2;
    # 		}
    # 	}

def p_pseudo_instruction_17(p):
    '''pseudo_instruction : PSEUDO_CALLBIOS value'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			write_byte(0xfd);
    # 			write_byte(0x2a);
    # 			write_word(0xfcc0);
    # 			write_byte(0xdd);
    # 			write_byte(0x21);
    # 			write_word($2);
    # 			write_byte(0xcd);
    # 			write_word(0x001c);
    # 		}
    # 	}

def p_pseudo_instruction_18(p):
    '''pseudo_instruction : PSEUDO_CALLDOS value'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			if (type != MSXDOS)
    # 			{
    # 				error_message(25, __FILE__, __LINE__);
    # 				exit(25);
    # 			}
    # 
    # 			write_byte(0x0e);
    # 			write_byte((char)$2);
    # 			write_byte(0xcd);
    # 			write_word(0x0005);
    # 		}
    # 	}

def p_pseudo_instruction_19(p):
    '''pseudo_instruction : PSEUDO_DB listing_8bits'''
    # {
    # 		;
    # 	}

def p_pseudo_instruction_20(p):
    '''pseudo_instruction : PSEUDO_DW listing_16bits'''
    # {
    # 		;
    # 	}

def p_pseudo_instruction_21(p):
    '''pseudo_instruction : PSEUDO_DS value_16bits'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			if (addr_start > PC)
    # 				addr_start = PC;
    # 			PC += $2;
    # 			ePC += $2;
    # 			if (PC > 0xffff)
    # 			{
    # 				error_message(1, __FILE__, __LINE__);
    # 				exit(1);
    # 			}
    # 		}
    # 	}

def p_pseudo_instruction_22(p):
    '''pseudo_instruction : PSEUDO_BYTE'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			PC++;
    # 			ePC++;
    # 		}
    # 	}

def p_pseudo_instruction_23(p):
    '''pseudo_instruction : PSEUDO_WORD'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			PC+=2;
    # 			ePC+=2;
    # 		}
    # 	}

def p_pseudo_instruction_24(p):
    '''pseudo_instruction : IDENTIFICATOR PSEUDO_EQU value'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			register_symbol(strtok($1, "="), $3, 2);
    # 		}
    # 	}

def p_pseudo_instruction_25(p):
    '''pseudo_instruction : IDENTIFICATOR PSEUDO_ASSIGN value'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			register_variable(strtok($1, "="), $3);
    # 		}
    # 	}

def p_pseudo_instruction_26(p):
    '''pseudo_instruction : PSEUDO_INCBIN TEXT'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			include_binary($2, 0, 0);
    # 		}
    # 	}

def p_pseudo_instruction_27(p):
    '''pseudo_instruction : PSEUDO_INCBIN TEXT PSEUDO_SKIP value'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			if ((int)($4) <= 0)
    # 			{
    # 				error_message(30, __FILE__, __LINE__);
    # 				exit(30);
    # 			}
    # 
    # 			include_binary($2, $4, 0);
    # 		}
    # 	}

def p_pseudo_instruction_28(p):
    '''pseudo_instruction : PSEUDO_INCBIN TEXT PSEUDO_SIZE value'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			if ((int)($4) <= 0)
    # 			{
    # 				error_message(30, __FILE__, __LINE__);
    # 				exit(30);
    # 			}
    # 
    # 			include_binary($2, 0, $4);
    # 		}
    # 	}

def p_pseudo_instruction_29(p):
    '''pseudo_instruction : PSEUDO_INCBIN TEXT PSEUDO_SKIP value PSEUDO_SIZE value'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			if (((int)($4) <= 0) || ((int)($6) <= 0))
    # 			{
    # 				error_message(30, __FILE__, __LINE__);
    # 				exit(30);
    # 			}
    # 
    # 			include_binary($2, $4, $6);
    # 		}
    # 	}

def p_pseudo_instruction_30(p):
    '''pseudo_instruction : PSEUDO_INCBIN TEXT PSEUDO_SIZE value PSEUDO_SKIP value'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			if (((int)($4) <= 0) || ((int)($6) <= 0))
    # 			{
    # 				error_message(30, __FILE__, __LINE__);
    # 				exit(30);
    # 			}
    # 
    # 			include_binary($2, $6, $4);
    # 		}
    # 	}

def p_pseudo_instruction_31(p):
    '''pseudo_instruction : PSEUDO_END'''
    # {
    # 		if (pass == 3)
    # 			finalize();
    # 		PC = 0;
    # 		ePC = 0;
    # 		last_global = 0;
    # 		type = 0;
    # 		zilog = 0;
    # 		if (conditional_level)
    # 		{
    # 			error_message(45, __FILE__, __LINE__);
    # 			exit(45);
    # 		}
    # 	}

def p_pseudo_instruction_32(p):
    '''pseudo_instruction : PSEUDO_DEBUG TEXT'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			write_byte(0x52);
    # 			write_byte(0x18);
    # 			write_byte(strlen($2) + 4);
    # 			write_text($2);
    # 		}
    # 	}

def p_pseudo_instruction_33(p):
    '''pseudo_instruction : PSEUDO_BREAK'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			write_byte(0x40);
    # 			write_byte(0x18);
    # 			write_byte(0x00);
    # 		}
    # 	}

def p_pseudo_instruction_34(p):
    '''pseudo_instruction : PSEUDO_BREAK value'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			write_byte(0x40);
    # 			write_byte(0x18);
    # 			write_byte(0x02);
    # 			write_word($2);
    # 		}
    # 	}

def p_pseudo_instruction_35(p):
    '''pseudo_instruction : PSEUDO_PRINTTEXT TEXT'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			if (pass == 2)
    # 			{
    # 				if (fmessages == NULL)
    # 					output_text();
    # 				fprintf(fmessages, "%s\n", $2);
    # 			}
    # 		}
    # 	}

def p_pseudo_instruction_36(p):
    '''pseudo_instruction : PSEUDO_PRINT value'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			if (pass == 2)
    # 			{
    # 				if (fmessages == NULL)
    # 					output_text();
    # 				fprintf(fmessages, "%d\n", (short)$2 & 0xffff);
    # 			}
    # 		}
    # 	}

def p_pseudo_instruction_37(p):
    '''pseudo_instruction : PSEUDO_PRINT value_real'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			if (pass == 2)
    # 			{
    # 				if (fmessages==NULL)
    # 					output_text();
    # 				fprintf(fmessages, "%.4f\n", $2);
    # 			}
    # 		}
    # 	}

def p_pseudo_instruction_38(p):
    '''pseudo_instruction : PSEUDO_PRINTHEX value'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			if (pass == 2)
    # 			{
    # 				if (fmessages == NULL)
    # 					output_text();
    # 				fprintf(fmessages, "$%4.4x\n", (short)$2 & 0xffff);
    # 			}
    # 		}
    # 	}

def p_pseudo_instruction_39(p):
    '''pseudo_instruction : PSEUDO_PRINTFIX value'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			if (pass == 2)
    # 			{
    # 				if (fmessages == NULL)
    # 					output_text();
    # 				fprintf(fmessages, "%.4f\n", ((float)($2 & 0xffff)) / 256);
    # 			}
    # 		}
    # 	}

def p_pseudo_instruction_40(p):
    '''pseudo_instruction : PSEUDO_SIZE value'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			if (pass == 2)
    # 			{
    # 				if (size > 0)
    # 				{
    # 					error_message(15, __FILE__, __LINE__);
    # 					exit(15);
    # 				}
    # 				else
    # 					size = $2;
    # 			}
    # 		}
    # 	}

def p_pseudo_instruction_41(p):
    '''pseudo_instruction : PSEUDO_IF value'''
    # {
    # 		if (conditional_level == 15)
    # 		{
    # 			error_message(44, __FILE__, __LINE__);
    # 			exit(44);
    # 		}
    # 
    # 		conditional_level++;
    # 
    # 		if ($2)
    # 			conditional[conditional_level] = 1 & conditional[conditional_level - 1];
    # 		else
    # 			conditional[conditional_level] = 0;
    # 	}

def p_pseudo_instruction_42(p):
    '''pseudo_instruction : PSEUDO_IFDEF IDENTIFICATOR'''
    # {
    # 		if (conditional_level == 15)
    # 		{
    # 			error_message(44, __FILE__, __LINE__);
    # 			exit(44);
    # 		}
    # 
    # 		conditional_level++;
    # 
    # 		if (defined_symbol($2))
    # 			conditional[conditional_level] = 1 & conditional[conditional_level - 1];
    # 		else
    # 			conditional[conditional_level] = 0;
    # 	}

def p_pseudo_instruction_43(p):
    '''pseudo_instruction : PSEUDO_ELSE'''
    # {
    # 		if (!conditional_level)
    # 		{
    # 			error_message(42, __FILE__, __LINE__);
    # 			exit(42);
    # 		}
    # 
    # 		conditional[conditional_level] = (conditional[conditional_level] ^ 1) & conditional[conditional_level - 1];
    # 	}

def p_pseudo_instruction_44(p):
    '''pseudo_instruction : PSEUDO_ENDIF'''
    # {
    # 		if (!conditional_level)
    # 		{
    # 			error_message(43, __FILE__, __LINE__);
    # 			exit(43);
    # 		}
    # 
    # 		conditional_level--;
    # 	}

def p_pseudo_instruction_45(p):
    '''pseudo_instruction : PSEUDO_CASSETTE TEXT'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			if (!intname[0])
    # 				strcpy(intname, $2);
    # 			cassette |= $1;
    # 		}
    # 	}

def p_pseudo_instruction_46(p):
    '''pseudo_instruction : PSEUDO_CASSETTE'''
    # {
    # 		if (conditional[conditional_level])
    # 		{
    # 			if (!intname[0])
    # 			{
    # 				strcpy(intname, binary);
    # 				intname[strlen(intname) - 1] = 0;
    # 			}
    # 			cassette |= $1;
    # 		}
    # 	}

def p_pseudo_instruction_47(p):
    '''pseudo_instruction : PSEUDO_ZILOG'''
    # {
    # 		zilog = 1;
    # 	}

def p_pseudo_instruction_48(p):
    '''pseudo_instruction : PSEUDO_FILENAME TEXT'''
    # {
    # 		strcpy(filename, $2);
    # 	}

def p_rel_IX_1(p):
    '''rel_IX : '[' REGISTER_16_IX ']''''
    # {
    # 		$$ = 0;
    # 	}

def p_rel_IX_2(p):
    '''rel_IX : '[' REGISTER_16_IX '+' value_8bits ']''''
    # {
    # 		$$ = $4;
    # 	}

def p_rel_IX_3(p):
    '''rel_IX : '[' REGISTER_16_IX '-' value_8bits ']''''
    # {
    # 		$$ = -((int)($4));
    # 	}

def p_rel_IY_1(p):
    '''rel_IY : '[' REGISTER_16_IY ']''''
    # {
    # 		$$ = 0;
    # 	}

def p_rel_IY_2(p):
    '''rel_IY : '[' REGISTER_16_IY '+' value_8bits ']''''
    # {
    # 		$$ = $4;
    # 	}

def p_rel_IY_3(p):
    '''rel_IY : '[' REGISTER_16_IY '-' value_8bits ']''''
    # {
    # 		$$ = -((int)($4));
    # 	}

def p_mnemo_load8bit_1(p):
    '''mnemo_load8bit : MNEMO_LD REGISTER ',' REGISTER'''
    # {
    # 		write_byte((char)(0x40 | ($2 << 3) | $4));
    # 	}

def p_mnemo_load8bit_2(p):
    '''mnemo_load8bit : MNEMO_LD REGISTER ',' REGISTER_IX'''
    # {
    # 		if (($2 > 3) && ($2 != 7))
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte((char)(0x40 | ($2 << 3) | $4));
    # 	}

def p_mnemo_load8bit_3(p):
    '''mnemo_load8bit : MNEMO_LD REGISTER_IX ',' REGISTER'''
    # {
    # 		if (($4 > 3) && ($4 != 7))
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte((char)(0x40 | ($2 << 3) | $4));
    # 	}

def p_mnemo_load8bit_4(p):
    '''mnemo_load8bit : MNEMO_LD REGISTER_IX ',' REGISTER_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte((char)(0x40 | ($2 << 3) | $4));
    # 	}

def p_mnemo_load8bit_5(p):
    '''mnemo_load8bit : MNEMO_LD REGISTER ',' REGISTER_IY'''
    # {
    # 		if (($2 > 3) && ($2 != 7))
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte((char)((0x40 | ($2 << 3) | $4)));
    # 	}

def p_mnemo_load8bit_6(p):
    '''mnemo_load8bit : MNEMO_LD REGISTER_IY ',' REGISTER'''
    # {
    # 		if (($4 > 3) && ($4 != 7))
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte((char)(0x40 | ($2 << 3) | $4));
    # 	}

def p_mnemo_load8bit_7(p):
    '''mnemo_load8bit : MNEMO_LD REGISTER_IY ',' REGISTER_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte((char)(0x40 | ($2 << 3) | $4));
    # 	}

def p_mnemo_load8bit_8(p):
    '''mnemo_load8bit : MNEMO_LD REGISTER ',' value_8bits'''
    # {
    # 		write_byte((char)(0x06 | ($2 << 3)));
    # 		write_byte((char)$4);
    # 	}

def p_mnemo_load8bit_9(p):
    '''mnemo_load8bit : MNEMO_LD REGISTER_IX ',' value_8bits'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte((char)(0x06 | ($2 << 3)));
    # 		write_byte((char)$4);
    # 	}

def p_mnemo_load8bit_10(p):
    '''mnemo_load8bit : MNEMO_LD REGISTER_IY ',' value_8bits'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte((char)(0x06 | ($2 << 3)));
    # 		write_byte((char)$4);
    # 	}

def p_mnemo_load8bit_11(p):
    '''mnemo_load8bit : MNEMO_LD REGISTER ',' REGISTER_IND_HL'''
    # {
    # 		write_byte((char)(0x46 | ($2 << 3)));
    # 	}

def p_mnemo_load8bit_12(p):
    '''mnemo_load8bit : MNEMO_LD REGISTER ',' rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte((char)(0x46 | ($2 << 3)));
    # 		write_byte((char)$4);
    # 	}

def p_mnemo_load8bit_13(p):
    '''mnemo_load8bit : MNEMO_LD REGISTER ',' rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte((char)(0x46 | ($2 << 3)));
    # 		write_byte((char)$4);
    # 	}

def p_mnemo_load8bit_14(p):
    '''mnemo_load8bit : MNEMO_LD REGISTER_IND_HL ',' REGISTER'''
    # {
    # 		write_byte((char)(0x70 | $4));
    # 	}

def p_mnemo_load8bit_15(p):
    '''mnemo_load8bit : MNEMO_LD rel_IX ',' REGISTER'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte((char)(0x70 | $4));
    # 		write_byte((char)$2);
    # 	}

def p_mnemo_load8bit_16(p):
    '''mnemo_load8bit : MNEMO_LD rel_IY ',' REGISTER'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte((char)(0x70 | $4));
    # 		write_byte((char)$2);
    # 	}

def p_mnemo_load8bit_17(p):
    '''mnemo_load8bit : MNEMO_LD REGISTER_IND_HL ',' value_8bits'''
    # {
    # 		write_byte(0x36);
    # 		write_byte((char)$4);
    # 	}

def p_mnemo_load8bit_18(p):
    '''mnemo_load8bit : MNEMO_LD rel_IX ',' value_8bits'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0x36);
    # 		write_byte((char)$2);
    # 		write_byte((char)$4);
    # 	}

def p_mnemo_load8bit_19(p):
    '''mnemo_load8bit : MNEMO_LD rel_IY ',' value_8bits'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0x36);
    # 		write_byte((char)$2);
    # 		write_byte((char)$4);
    # 	}

def p_mnemo_load8bit_20(p):
    '''mnemo_load8bit : MNEMO_LD REGISTER ',' REGISTER_IND_BC'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0x0a);
    # 	}

def p_mnemo_load8bit_21(p):
    '''mnemo_load8bit : MNEMO_LD REGISTER ',' REGISTER_IND_DE'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0x1a);
    # 	}

def p_mnemo_load8bit_22(p):
    '''mnemo_load8bit : MNEMO_LD REGISTER ',' '[' value_16bits ']''''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0x3a);
    # 		write_word($5);
    # 	}

def p_mnemo_load8bit_23(p):
    '''mnemo_load8bit : MNEMO_LD REGISTER_IND_BC ',' REGISTER'''
    # {
    # 		if ($4 != 7)
    # 		{
    # 			error_message(5, __FILE__, __LINE__);
    # 			exit(5);
    # 		}
    # 
    # 		write_byte(0x02);
    # 	}

def p_mnemo_load8bit_24(p):
    '''mnemo_load8bit : MNEMO_LD REGISTER_IND_DE ',' REGISTER'''
    # {
    # 		if ($4 != 7)
    # 		{
    # 			error_message(5, __FILE__, __LINE__);
    # 			exit(5);
    # 		}
    # 
    # 		write_byte(0x12);
    # 	}

def p_mnemo_load8bit_25(p):
    '''mnemo_load8bit : MNEMO_LD '[' value_16bits ']' ',' REGISTER'''
    # {
    # 		if ($6 != 7)
    # 		{
    # 			error_message(5, __FILE__, __LINE__);
    # 			exit(5);
    # 		}
    # 
    # 		write_byte(0x32);
    # 		write_word($3);
    # 	}

def p_mnemo_load8bit_26(p):
    '''mnemo_load8bit : MNEMO_LD REGISTER ',' REGISTER_I'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0xed);
    # 		write_byte(0x57);
    # 	}

def p_mnemo_load8bit_27(p):
    '''mnemo_load8bit : MNEMO_LD REGISTER ',' REGISTER_R'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0xed);
    # 		write_byte(0x5f);
    # 	}

def p_mnemo_load8bit_28(p):
    '''mnemo_load8bit : MNEMO_LD REGISTER_I ',' REGISTER'''
    # {
    # 		if ($4 != 7)
    # 		{
    # 			error_message(5, __FILE__, __LINE__);
    # 			exit(5);
    # 		}
    # 
    # 		write_byte(0xed);
    # 		write_byte(0x47);
    # 	}

def p_mnemo_load8bit_29(p):
    '''mnemo_load8bit : MNEMO_LD REGISTER_R ',' REGISTER'''
    # {
    # 		if ($4 != 7)
    # 		{
    # 			error_message(5, __FILE__, __LINE__);
    # 			exit(5);
    # 		}
    # 
    # 		write_byte(0xed);
    # 		write_byte(0x4f);
    # 	}

def p_mnemo_load16bit_1(p):
    '''mnemo_load16bit : MNEMO_LD REGISTER_PAR ',' value_16bits'''
    # {
    # 		write_byte(0x01 | ($2 << 4));
    # 		write_word($4);
    # 	}

def p_mnemo_load16bit_2(p):
    '''mnemo_load16bit : MNEMO_LD REGISTER_16_IX ',' value_16bits'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0x21);
    # 		write_word($4);
    # 	}

def p_mnemo_load16bit_3(p):
    '''mnemo_load16bit : MNEMO_LD REGISTER_16_IY ',' value_16bits'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0x21);
    # 		write_word($4);
    # 	}

def p_mnemo_load16bit_4(p):
    '''mnemo_load16bit : MNEMO_LD REGISTER_PAR ',' '[' value_16bits ']''''
    # {
    # 		if ($2 != 2)
    # 		{
    # 			write_byte(0xed);
    # 			write_byte(0x4b | ($2 << 4));
    # 		}
    # 		else
    # 			write_byte(0x2a);
    # 		write_word($5);
    # 	}

def p_mnemo_load16bit_5(p):
    '''mnemo_load16bit : MNEMO_LD REGISTER_16_IX ',' '[' value_16bits ']''''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0x2a);
    # 		write_word($5);
    # 	}

def p_mnemo_load16bit_6(p):
    '''mnemo_load16bit : MNEMO_LD REGISTER_16_IY ',' '[' value_16bits ']''''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0x2a);
    # 		write_word($5);
    # 	}

def p_mnemo_load16bit_7(p):
    '''mnemo_load16bit : MNEMO_LD '[' value_16bits ']' ',' REGISTER_PAR'''
    # {
    # 		if ($6 != 2)
    # 		{
    # 			write_byte(0xed);
    # 			write_byte(0x43 | ($6 << 4));
    # 		}
    # 		else
    # 			write_byte(0x22);
    # 		write_word($3);
    # 	}

def p_mnemo_load16bit_8(p):
    '''mnemo_load16bit : MNEMO_LD '[' value_16bits ']' ',' REGISTER_16_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0x22);
    # 		write_word($3);
    # 	}

def p_mnemo_load16bit_9(p):
    '''mnemo_load16bit : MNEMO_LD '[' value_16bits ']' ',' REGISTER_16_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0x22);
    # 		write_word($3);
    # 	}

def p_mnemo_load16bit_10(p):
    '''mnemo_load16bit : MNEMO_LD_SP ',' '[' value_16bits ']''''
    # {
    # 		write_byte(0xed);
    # 		write_byte(0x7b);
    # 		write_word($4);
    # 	}

def p_mnemo_load16bit_11(p):
    '''mnemo_load16bit : MNEMO_LD_SP ',' value_16bits'''
    # {
    # 		write_byte(0x31);
    # 		write_word($3);
    # 	}

def p_mnemo_load16bit_12(p):
    '''mnemo_load16bit : MNEMO_LD_SP ',' REGISTER_PAR'''
    # {
    # 		if ($3 != 2)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xf9);
    # 	}

def p_mnemo_load16bit_13(p):
    '''mnemo_load16bit : MNEMO_LD_SP ',' REGISTER_16_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xf9);
    # 	}

def p_mnemo_load16bit_14(p):
    '''mnemo_load16bit : MNEMO_LD_SP ',' REGISTER_16_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xf9);
    # 	}

def p_mnemo_load16bit_15(p):
    '''mnemo_load16bit : MNEMO_PUSH REGISTER_PAR'''
    # {
    # 		if ($2 == 3)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xc5 | ($2 << 4));
    # 	}

def p_mnemo_load16bit_16(p):
    '''mnemo_load16bit : MNEMO_PUSH REGISTER_AF'''
    # {
    # 		write_byte(0xf5);
    # 	}

def p_mnemo_load16bit_17(p):
    '''mnemo_load16bit : MNEMO_PUSH REGISTER_16_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xe5);
    # 	}

def p_mnemo_load16bit_18(p):
    '''mnemo_load16bit : MNEMO_PUSH REGISTER_16_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xe5);
    # 	}

def p_mnemo_load16bit_19(p):
    '''mnemo_load16bit : MNEMO_POP REGISTER_PAR'''
    # {
    # 		if ($2 == 3)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xc1 | ($2 << 4));
    # 	}

def p_mnemo_load16bit_20(p):
    '''mnemo_load16bit : MNEMO_POP REGISTER_AF'''
    # {
    # 		write_byte(0xf1);
    # 	}

def p_mnemo_load16bit_21(p):
    '''mnemo_load16bit : MNEMO_POP REGISTER_16_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xe1);
    # 	}

def p_mnemo_load16bit_22(p):
    '''mnemo_load16bit : MNEMO_POP REGISTER_16_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xe1);
    # 	}

def p_mnemo_exchange_1(p):
    '''mnemo_exchange : MNEMO_EX REGISTER_PAR ',' REGISTER_PAR'''
    # {
    # 		if ((($2 != 1) || ($4 != 2)) && (($2 != 2) || ($4 != 1)))
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		if ((zilog) && ($2 != 1))
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 		write_byte(0xeb);
    # 	}

def p_mnemo_exchange_2(p):
    '''mnemo_exchange : MNEMO_EX REGISTER_AF ',' REGISTER_AF APOSTROPHE'''
    # {
    # 		write_byte(0x08);
    # 	}

def p_mnemo_exchange_3(p):
    '''mnemo_exchange : MNEMO_EXX'''
    # {
    # 		write_byte(0xd9);
    # 	}

def p_mnemo_exchange_4(p):
    '''mnemo_exchange : MNEMO_EX REGISTER_IND_SP ',' REGISTER_PAR'''
    # {
    # 		if ($4 != 2)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xe3);
    # 	}

def p_mnemo_exchange_5(p):
    '''mnemo_exchange : MNEMO_EX REGISTER_IND_SP ',' REGISTER_16_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xe3);
    # 	}

def p_mnemo_exchange_6(p):
    '''mnemo_exchange : MNEMO_EX REGISTER_IND_SP ',' REGISTER_16_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xe3);
    # 	}

def p_mnemo_exchange_7(p):
    '''mnemo_exchange : MNEMO_LDI'''
    # {
    # 		write_byte(0xed);
    # 		write_byte(0xa0);
    # 	}

def p_mnemo_exchange_8(p):
    '''mnemo_exchange : MNEMO_LDIR'''
    # {
    # 		write_byte(0xed);
    # 		write_byte(0xb0);
    # 	}

def p_mnemo_exchange_9(p):
    '''mnemo_exchange : MNEMO_LDD'''
    # {
    # 		write_byte(0xed);
    # 		write_byte(0xa8);
    # 	}

def p_mnemo_exchange_10(p):
    '''mnemo_exchange : MNEMO_LDDR'''
    # {
    # 		write_byte(0xed);
    # 		write_byte(0xb8);
    # 	}

def p_mnemo_exchange_11(p):
    '''mnemo_exchange : MNEMO_CPI'''
    # {
    # 		write_byte(0xed);
    # 		write_byte(0xa1);
    # 	}

def p_mnemo_exchange_12(p):
    '''mnemo_exchange : MNEMO_CPIR'''
    # {
    # 		write_byte(0xed);
    # 		write_byte(0xb1);
    # 	}

def p_mnemo_exchange_13(p):
    '''mnemo_exchange : MNEMO_CPD'''
    # {
    # 		write_byte(0xed);
    # 		write_byte(0xa9);
    # 	}

def p_mnemo_exchange_14(p):
    '''mnemo_exchange : MNEMO_CPDR'''
    # {
    # 		write_byte(0xed);
    # 		write_byte(0xb9);
    # 	}

def p_mnemo_arithm8bit_1(p):
    '''mnemo_arithm8bit : MNEMO_ADD REGISTER ',' REGISTER'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0x80 | $4);
    # 	}

def p_mnemo_arithm8bit_2(p):
    '''mnemo_arithm8bit : MNEMO_ADD REGISTER ',' REGISTER_IX'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0x80 | $4);
    # 	}

def p_mnemo_arithm8bit_3(p):
    '''mnemo_arithm8bit : MNEMO_ADD REGISTER ',' REGISTER_IY'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0x80 | $4);
    # 	}

def p_mnemo_arithm8bit_4(p):
    '''mnemo_arithm8bit : MNEMO_ADD REGISTER ',' value_8bits'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0xc6);
    # 		write_byte($4);
    # 	}

def p_mnemo_arithm8bit_5(p):
    '''mnemo_arithm8bit : MNEMO_ADD REGISTER ',' REGISTER_IND_HL'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0x86);
    # 	}

def p_mnemo_arithm8bit_6(p):
    '''mnemo_arithm8bit : MNEMO_ADD REGISTER ',' rel_IX'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0x86);
    # 		write_byte($4);
    # 	}

def p_mnemo_arithm8bit_7(p):
    '''mnemo_arithm8bit : MNEMO_ADD REGISTER ',' rel_IY'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0x86);
    # 		write_byte($4);
    # 	}

def p_mnemo_arithm8bit_8(p):
    '''mnemo_arithm8bit : MNEMO_ADC REGISTER ',' REGISTER'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0x88 | $4);
    # 	}

def p_mnemo_arithm8bit_9(p):
    '''mnemo_arithm8bit : MNEMO_ADC REGISTER ',' REGISTER_IX'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0x88 | $4);
    # 	}

def p_mnemo_arithm8bit_10(p):
    '''mnemo_arithm8bit : MNEMO_ADC REGISTER ',' REGISTER_IY'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0x88 | $4);
    # 	}

def p_mnemo_arithm8bit_11(p):
    '''mnemo_arithm8bit : MNEMO_ADC REGISTER ',' value_8bits'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0xce);
    # 		write_byte($4);
    # 	}

def p_mnemo_arithm8bit_12(p):
    '''mnemo_arithm8bit : MNEMO_ADC REGISTER ',' REGISTER_IND_HL'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0x8e);
    # 	}

def p_mnemo_arithm8bit_13(p):
    '''mnemo_arithm8bit : MNEMO_ADC REGISTER ',' rel_IX'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0x8e);
    # 		write_byte($4);
    # 	}

def p_mnemo_arithm8bit_14(p):
    '''mnemo_arithm8bit : MNEMO_ADC REGISTER ',' rel_IY'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0x8e);
    # 		write_byte($4);
    # 	}

def p_mnemo_arithm8bit_15(p):
    '''mnemo_arithm8bit : MNEMO_SUB REGISTER ',' REGISTER'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0x90 | $4);
    # 	}

def p_mnemo_arithm8bit_16(p):
    '''mnemo_arithm8bit : MNEMO_SUB REGISTER ',' REGISTER_IX'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0x90 | $4);
    # 	}

def p_mnemo_arithm8bit_17(p):
    '''mnemo_arithm8bit : MNEMO_SUB REGISTER ',' REGISTER_IY'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0x90 | $4);
    # 	}

def p_mnemo_arithm8bit_18(p):
    '''mnemo_arithm8bit : MNEMO_SUB REGISTER ',' value_8bits'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xd6);
    # 		write_byte($4);
    # 	}

def p_mnemo_arithm8bit_19(p):
    '''mnemo_arithm8bit : MNEMO_SUB REGISTER ',' REGISTER_IND_HL'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0x96);
    # 	}

def p_mnemo_arithm8bit_20(p):
    '''mnemo_arithm8bit : MNEMO_SUB REGISTER ',' rel_IX'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0x96);
    # 		write_byte($4);
    # 	}

def p_mnemo_arithm8bit_21(p):
    '''mnemo_arithm8bit : MNEMO_SUB REGISTER ',' rel_IY'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0x96);
    # 		write_byte($4);
    # 	}

def p_mnemo_arithm8bit_22(p):
    '''mnemo_arithm8bit : MNEMO_SBC REGISTER ',' REGISTER'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0x98 | $4);
    # 	}

def p_mnemo_arithm8bit_23(p):
    '''mnemo_arithm8bit : MNEMO_SBC REGISTER ',' REGISTER_IX'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0x98 | $4);
    # 	}

def p_mnemo_arithm8bit_24(p):
    '''mnemo_arithm8bit : MNEMO_SBC REGISTER ',' REGISTER_IY'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0x98 | $4);
    # 	}

def p_mnemo_arithm8bit_25(p):
    '''mnemo_arithm8bit : MNEMO_SBC REGISTER ',' value_8bits'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0xde);
    # 		write_byte($4);
    # 	}

def p_mnemo_arithm8bit_26(p):
    '''mnemo_arithm8bit : MNEMO_SBC REGISTER ',' REGISTER_IND_HL'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0x9e);
    # 	}

def p_mnemo_arithm8bit_27(p):
    '''mnemo_arithm8bit : MNEMO_SBC REGISTER ',' rel_IX'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0x9e);
    # 		write_byte($4);
    # 	}

def p_mnemo_arithm8bit_28(p):
    '''mnemo_arithm8bit : MNEMO_SBC REGISTER ',' rel_IY'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0x9e);
    # 		write_byte($4);
    # 	}

def p_mnemo_arithm8bit_29(p):
    '''mnemo_arithm8bit : MNEMO_AND REGISTER ',' REGISTER'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xa0 | $4);
    # 	}

def p_mnemo_arithm8bit_30(p):
    '''mnemo_arithm8bit : MNEMO_AND REGISTER ',' REGISTER_IX'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0xa0 | $4);
    # 	}

def p_mnemo_arithm8bit_31(p):
    '''mnemo_arithm8bit : MNEMO_AND REGISTER ',' REGISTER_IY'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0xa0 | $4);
    # 	}

def p_mnemo_arithm8bit_32(p):
    '''mnemo_arithm8bit : MNEMO_AND REGISTER ',' value_8bits'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xe6);
    # 		write_byte($4);
    # 	}

def p_mnemo_arithm8bit_33(p):
    '''mnemo_arithm8bit : MNEMO_AND REGISTER ',' REGISTER_IND_HL'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xa6);
    # 	}

def p_mnemo_arithm8bit_34(p):
    '''mnemo_arithm8bit : MNEMO_AND REGISTER ',' rel_IX'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0xa6);
    # 		write_byte($4);
    # 	}

def p_mnemo_arithm8bit_35(p):
    '''mnemo_arithm8bit : MNEMO_AND REGISTER ',' rel_IY'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0xa6);
    # 		write_byte($4);
    # 	}

def p_mnemo_arithm8bit_36(p):
    '''mnemo_arithm8bit : MNEMO_OR REGISTER ',' REGISTER'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xb0 | $4);
    # 	}

def p_mnemo_arithm8bit_37(p):
    '''mnemo_arithm8bit : MNEMO_OR REGISTER ',' REGISTER_IX'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0xb0 | $4);
    # 	}

def p_mnemo_arithm8bit_38(p):
    '''mnemo_arithm8bit : MNEMO_OR REGISTER ',' REGISTER_IY'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0xb0 | $4);
    # 	}

def p_mnemo_arithm8bit_39(p):
    '''mnemo_arithm8bit : MNEMO_OR REGISTER ',' value_8bits'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xf6);
    # 		write_byte($4);
    # 	}

def p_mnemo_arithm8bit_40(p):
    '''mnemo_arithm8bit : MNEMO_OR REGISTER ',' REGISTER_IND_HL'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xb6);
    # 	}

def p_mnemo_arithm8bit_41(p):
    '''mnemo_arithm8bit : MNEMO_OR REGISTER ',' rel_IX'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0xb6);
    # 		write_byte($4);
    # 	}

def p_mnemo_arithm8bit_42(p):
    '''mnemo_arithm8bit : MNEMO_OR REGISTER ',' rel_IY'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0xb6);
    # 		write_byte($4);
    # 	}

def p_mnemo_arithm8bit_43(p):
    '''mnemo_arithm8bit : MNEMO_XOR REGISTER ',' REGISTER'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xa8 | $4);
    # 	}

def p_mnemo_arithm8bit_44(p):
    '''mnemo_arithm8bit : MNEMO_XOR REGISTER ',' REGISTER_IX'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0xa8 | $4);
    # 	}

def p_mnemo_arithm8bit_45(p):
    '''mnemo_arithm8bit : MNEMO_XOR REGISTER ',' REGISTER_IY'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0xa8 | $4);
    # 	}

def p_mnemo_arithm8bit_46(p):
    '''mnemo_arithm8bit : MNEMO_XOR REGISTER ',' value_8bits'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xee);
    # 		write_byte($4);
    # 	}

def p_mnemo_arithm8bit_47(p):
    '''mnemo_arithm8bit : MNEMO_XOR REGISTER ',' REGISTER_IND_HL'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xae);
    # 	}

def p_mnemo_arithm8bit_48(p):
    '''mnemo_arithm8bit : MNEMO_XOR REGISTER ',' rel_IX'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0xae);
    # 		write_byte($4);
    # 	}

def p_mnemo_arithm8bit_49(p):
    '''mnemo_arithm8bit : MNEMO_XOR REGISTER ',' rel_IY'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0xae);
    # 		write_byte($4);
    # 	}

def p_mnemo_arithm8bit_50(p):
    '''mnemo_arithm8bit : MNEMO_CP REGISTER ',' REGISTER'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xb8 | $4);
    # 	}

def p_mnemo_arithm8bit_51(p):
    '''mnemo_arithm8bit : MNEMO_CP REGISTER ',' REGISTER_IX'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0xb8 | $4);
    # 	}

def p_mnemo_arithm8bit_52(p):
    '''mnemo_arithm8bit : MNEMO_CP REGISTER ',' REGISTER_IY'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0xb8 | $4);
    # 	}

def p_mnemo_arithm8bit_53(p):
    '''mnemo_arithm8bit : MNEMO_CP REGISTER ',' value_8bits'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xfe);
    # 		write_byte($4);
    # 	}

def p_mnemo_arithm8bit_54(p):
    '''mnemo_arithm8bit : MNEMO_CP REGISTER ',' REGISTER_IND_HL'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xbe);
    # 	}

def p_mnemo_arithm8bit_55(p):
    '''mnemo_arithm8bit : MNEMO_CP REGISTER ',' rel_IX'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0xbe);
    # 		write_byte($4);
    # 	}

def p_mnemo_arithm8bit_56(p):
    '''mnemo_arithm8bit : MNEMO_CP REGISTER ',' rel_IY'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0xbe);
    # 		write_byte($4);
    # 	}

def p_mnemo_arithm8bit_57(p):
    '''mnemo_arithm8bit : MNEMO_ADD REGISTER'''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0x80 | $2);
    # 	}

def p_mnemo_arithm8bit_58(p):
    '''mnemo_arithm8bit : MNEMO_ADD REGISTER_IX'''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0x80 | $2);
    # 	}

def p_mnemo_arithm8bit_59(p):
    '''mnemo_arithm8bit : MNEMO_ADD REGISTER_IY'''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0x80 | $2);
    # 	}

def p_mnemo_arithm8bit_60(p):
    '''mnemo_arithm8bit : MNEMO_ADD value_8bits'''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xc6);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_61(p):
    '''mnemo_arithm8bit : MNEMO_ADD REGISTER_IND_HL'''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0x86);
    # 	}

def p_mnemo_arithm8bit_62(p):
    '''mnemo_arithm8bit : MNEMO_ADD rel_IX'''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0x86);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_63(p):
    '''mnemo_arithm8bit : MNEMO_ADD rel_IY'''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0x86);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_64(p):
    '''mnemo_arithm8bit : MNEMO_ADC REGISTER'''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0x88 | $2);
    # 	}

def p_mnemo_arithm8bit_65(p):
    '''mnemo_arithm8bit : MNEMO_ADC REGISTER_IX'''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0x88 | $2);
    # 	}

def p_mnemo_arithm8bit_66(p):
    '''mnemo_arithm8bit : MNEMO_ADC REGISTER_IY'''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0x88 | $2);
    # 	}

def p_mnemo_arithm8bit_67(p):
    '''mnemo_arithm8bit : MNEMO_ADC value_8bits'''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xce);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_68(p):
    '''mnemo_arithm8bit : MNEMO_ADC REGISTER_IND_HL'''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0x8e);
    # 	}

def p_mnemo_arithm8bit_69(p):
    '''mnemo_arithm8bit : MNEMO_ADC rel_IX'''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0x8e);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_70(p):
    '''mnemo_arithm8bit : MNEMO_ADC rel_IY'''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0x8e);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_71(p):
    '''mnemo_arithm8bit : MNEMO_SUB REGISTER'''
    # {
    # 		write_byte(0x90 | $2);
    # 	}

def p_mnemo_arithm8bit_72(p):
    '''mnemo_arithm8bit : MNEMO_SUB REGISTER_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0x90 | $2);
    # 	}

def p_mnemo_arithm8bit_73(p):
    '''mnemo_arithm8bit : MNEMO_SUB REGISTER_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0x90 | $2);
    # 	}

def p_mnemo_arithm8bit_74(p):
    '''mnemo_arithm8bit : MNEMO_SUB value_8bits'''
    # {
    # 		write_byte(0xd6);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_75(p):
    '''mnemo_arithm8bit : MNEMO_SUB REGISTER_IND_HL'''
    # {
    # 		write_byte(0x96);
    # 	}

def p_mnemo_arithm8bit_76(p):
    '''mnemo_arithm8bit : MNEMO_SUB rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0x96);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_77(p):
    '''mnemo_arithm8bit : MNEMO_SUB rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0x96);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_78(p):
    '''mnemo_arithm8bit : MNEMO_SBC REGISTER'''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0x98 | $2);
    # 	}

def p_mnemo_arithm8bit_79(p):
    '''mnemo_arithm8bit : MNEMO_SBC REGISTER_IX'''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0x98 | $2);
    # 	}

def p_mnemo_arithm8bit_80(p):
    '''mnemo_arithm8bit : MNEMO_SBC REGISTER_IY'''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0x98 | $2);
    # 	}

def p_mnemo_arithm8bit_81(p):
    '''mnemo_arithm8bit : MNEMO_SBC value_8bits'''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xde);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_82(p):
    '''mnemo_arithm8bit : MNEMO_SBC REGISTER_IND_HL'''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0x9e);
    # 	}

def p_mnemo_arithm8bit_83(p):
    '''mnemo_arithm8bit : MNEMO_SBC rel_IX'''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0x9e);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_84(p):
    '''mnemo_arithm8bit : MNEMO_SBC rel_IY'''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0x9e);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_85(p):
    '''mnemo_arithm8bit : MNEMO_AND REGISTER'''
    # {
    # 		write_byte(0xa0 | $2);
    # 	}

def p_mnemo_arithm8bit_86(p):
    '''mnemo_arithm8bit : MNEMO_AND REGISTER_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xa0 | $2);
    # 	}

def p_mnemo_arithm8bit_87(p):
    '''mnemo_arithm8bit : MNEMO_AND REGISTER_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xa0 | $2);
    # 	}

def p_mnemo_arithm8bit_88(p):
    '''mnemo_arithm8bit : MNEMO_AND value_8bits'''
    # {
    # 		write_byte(0xe6);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_89(p):
    '''mnemo_arithm8bit : MNEMO_AND REGISTER_IND_HL'''
    # {
    # 		write_byte(0xa6);
    # 	}

def p_mnemo_arithm8bit_90(p):
    '''mnemo_arithm8bit : MNEMO_AND rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xa6);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_91(p):
    '''mnemo_arithm8bit : MNEMO_AND rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xa6);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_92(p):
    '''mnemo_arithm8bit : MNEMO_OR REGISTER'''
    # {
    # 		write_byte(0xb0 | $2);
    # 	}

def p_mnemo_arithm8bit_93(p):
    '''mnemo_arithm8bit : MNEMO_OR REGISTER_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xb0 | $2);
    # 	}

def p_mnemo_arithm8bit_94(p):
    '''mnemo_arithm8bit : MNEMO_OR REGISTER_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xb0 | $2);
    # 	}

def p_mnemo_arithm8bit_95(p):
    '''mnemo_arithm8bit : MNEMO_OR value_8bits'''
    # {
    # 		write_byte(0xf6);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_96(p):
    '''mnemo_arithm8bit : MNEMO_OR REGISTER_IND_HL'''
    # {
    # 		write_byte(0xb6);
    # 	}

def p_mnemo_arithm8bit_97(p):
    '''mnemo_arithm8bit : MNEMO_OR rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xb6);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_98(p):
    '''mnemo_arithm8bit : MNEMO_OR rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xb6);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_99(p):
    '''mnemo_arithm8bit : MNEMO_XOR REGISTER'''
    # {
    # 		write_byte(0xa8 | $2);
    # 	}

def p_mnemo_arithm8bit_100(p):
    '''mnemo_arithm8bit : MNEMO_XOR REGISTER_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xa8 | $2);
    # 	}

def p_mnemo_arithm8bit_101(p):
    '''mnemo_arithm8bit : MNEMO_XOR REGISTER_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xa8 | $2);
    # 	}

def p_mnemo_arithm8bit_102(p):
    '''mnemo_arithm8bit : MNEMO_XOR value_8bits'''
    # {
    # 		write_byte(0xee);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_103(p):
    '''mnemo_arithm8bit : MNEMO_XOR REGISTER_IND_HL'''
    # {
    # 		write_byte(0xae);
    # 	}

def p_mnemo_arithm8bit_104(p):
    '''mnemo_arithm8bit : MNEMO_XOR rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xae);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_105(p):
    '''mnemo_arithm8bit : MNEMO_XOR rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xae);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_106(p):
    '''mnemo_arithm8bit : MNEMO_CP REGISTER'''
    # {
    # 		write_byte(0xb8 | $2);
    # 	}

def p_mnemo_arithm8bit_107(p):
    '''mnemo_arithm8bit : MNEMO_CP REGISTER_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xb8 | $2);
    # 	}

def p_mnemo_arithm8bit_108(p):
    '''mnemo_arithm8bit : MNEMO_CP REGISTER_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xb8 | $2);
    # 	}

def p_mnemo_arithm8bit_109(p):
    '''mnemo_arithm8bit : MNEMO_CP value_8bits'''
    # {
    # 		write_byte(0xfe);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_110(p):
    '''mnemo_arithm8bit : MNEMO_CP REGISTER_IND_HL'''
    # {
    # 		write_byte(0xbe);
    # 	}

def p_mnemo_arithm8bit_111(p):
    '''mnemo_arithm8bit : MNEMO_CP rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xbe);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_112(p):
    '''mnemo_arithm8bit : MNEMO_CP rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xbe);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_113(p):
    '''mnemo_arithm8bit : MNEMO_INC REGISTER'''
    # {
    # 		write_byte(0x04 | ($2 << 3));
    # 	}

def p_mnemo_arithm8bit_114(p):
    '''mnemo_arithm8bit : MNEMO_INC REGISTER_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0x04 | ($2 << 3));
    # 	}

def p_mnemo_arithm8bit_115(p):
    '''mnemo_arithm8bit : MNEMO_INC REGISTER_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0x04 | ($2 << 3));
    # 	}

def p_mnemo_arithm8bit_116(p):
    '''mnemo_arithm8bit : MNEMO_INC REGISTER_IND_HL'''
    # {
    # 		write_byte(0x34);
    # 	}

def p_mnemo_arithm8bit_117(p):
    '''mnemo_arithm8bit : MNEMO_INC rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0x34);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_118(p):
    '''mnemo_arithm8bit : MNEMO_INC rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0x34);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_119(p):
    '''mnemo_arithm8bit : MNEMO_DEC REGISTER'''
    # {
    # 		write_byte(0x05 | ($2 << 3));
    # 	}

def p_mnemo_arithm8bit_120(p):
    '''mnemo_arithm8bit : MNEMO_DEC REGISTER_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0x05 | ($2 << 3));
    # 	}

def p_mnemo_arithm8bit_121(p):
    '''mnemo_arithm8bit : MNEMO_DEC REGISTER_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0x05 | ($2 << 3));
    # 	}

def p_mnemo_arithm8bit_122(p):
    '''mnemo_arithm8bit : MNEMO_DEC REGISTER_IND_HL'''
    # {
    # 		write_byte(0x35);
    # 	}

def p_mnemo_arithm8bit_123(p):
    '''mnemo_arithm8bit : MNEMO_DEC rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0x35);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm8bit_124(p):
    '''mnemo_arithm8bit : MNEMO_DEC rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0x35);
    # 		write_byte($2);
    # 	}

def p_mnemo_arithm16bit_1(p):
    '''mnemo_arithm16bit : MNEMO_ADD REGISTER_PAR ',' REGISTER_PAR'''
    # {
    # 		if ($2 != 2)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0x09 | ($4 << 4));
    # 	}

def p_mnemo_arithm16bit_2(p):
    '''mnemo_arithm16bit : MNEMO_ADC REGISTER_PAR ',' REGISTER_PAR'''
    # {
    # 		if ($2 != 2)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xed);
    # 		write_byte(0x4a | ($4 << 4));
    # 	}

def p_mnemo_arithm16bit_3(p):
    '''mnemo_arithm16bit : MNEMO_SBC REGISTER_PAR ',' REGISTER_PAR'''
    # {
    # 		if ($2 != 2)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xed);
    # 		write_byte(0x42 | ($4 << 4));
    # 	}

def p_mnemo_arithm16bit_4(p):
    '''mnemo_arithm16bit : MNEMO_ADD REGISTER_16_IX ',' REGISTER_PAR'''
    # {
    # 		if ($4 == 2)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0x09 | ($4 << 4));
    # 	}

def p_mnemo_arithm16bit_5(p):
    '''mnemo_arithm16bit : MNEMO_ADD REGISTER_16_IX ',' REGISTER_16_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0x29);
    # 	}

def p_mnemo_arithm16bit_6(p):
    '''mnemo_arithm16bit : MNEMO_ADD REGISTER_16_IY ',' REGISTER_PAR'''
    # {
    # 		if ($4 == 2)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0x09 | ($4 << 4));
    # 	}

def p_mnemo_arithm16bit_7(p):
    '''mnemo_arithm16bit : MNEMO_ADD REGISTER_16_IY ',' REGISTER_16_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0x29);
    # 	}

def p_mnemo_arithm16bit_8(p):
    '''mnemo_arithm16bit : MNEMO_INC REGISTER_PAR'''
    # {
    # 		write_byte(0x03 | ($2 << 4));
    # 	}

def p_mnemo_arithm16bit_9(p):
    '''mnemo_arithm16bit : MNEMO_INC REGISTER_16_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0x23);
    # 	}

def p_mnemo_arithm16bit_10(p):
    '''mnemo_arithm16bit : MNEMO_INC REGISTER_16_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0x23);
    # 	}

def p_mnemo_arithm16bit_11(p):
    '''mnemo_arithm16bit : MNEMO_DEC REGISTER_PAR'''
    # {
    # 		write_byte(0x0b | ($2 << 4));
    # 	}

def p_mnemo_arithm16bit_12(p):
    '''mnemo_arithm16bit : MNEMO_DEC REGISTER_16_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0x2b);
    # 	}

def p_mnemo_arithm16bit_13(p):
    '''mnemo_arithm16bit : MNEMO_DEC REGISTER_16_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0x2b);
    # 	}

def p_mnemo_general_1(p):
    '''mnemo_general : MNEMO_DAA'''
    # {
    # 		write_byte(0x27);
    # 	}

def p_mnemo_general_2(p):
    '''mnemo_general : MNEMO_CPL'''
    # {
    # 		write_byte(0x2f);
    # 	}

def p_mnemo_general_3(p):
    '''mnemo_general : MNEMO_NEG'''
    # {
    # 		write_byte(0xed);
    # 		write_byte(0x44);
    # 	}

def p_mnemo_general_4(p):
    '''mnemo_general : MNEMO_CCF'''
    # {
    # 		write_byte(0x3f);
    # 	}

def p_mnemo_general_5(p):
    '''mnemo_general : MNEMO_SCF'''
    # {
    # 		write_byte(0x37);
    # 	}

def p_mnemo_general_6(p):
    '''mnemo_general : MNEMO_NOP'''
    # {
    # 		write_byte(0x00);
    # 	}

def p_mnemo_general_7(p):
    '''mnemo_general : MNEMO_HALT'''
    # {
    # 		write_byte(0x76);
    # 	}

def p_mnemo_general_8(p):
    '''mnemo_general : MNEMO_DI'''
    # {
    # 		write_byte(0xf3);
    # 	}

def p_mnemo_general_9(p):
    '''mnemo_general : MNEMO_EI'''
    # {
    # 		write_byte(0xfb);
    # 	}

def p_mnemo_general_10(p):
    '''mnemo_general : MNEMO_IM value_8bits'''
    # {
    # 		if (((int)($2) < 0) || ((int)($2) > 2))
    # 		{
    # 			error_message(3, __FILE__, __LINE__);
    # 			exit(3);
    # 		}
    # 
    # 		write_byte(0xed);
    # 
    # 		if ($2 == 0)
    # 			write_byte(0x46);
    # 		else
    # 			if ($2 == 1)
    # 				write_byte(0x56);
    # 			else
    # 				write_byte(0x5e);
    # 	}

def p_mnemo_rotate_1(p):
    '''mnemo_rotate : MNEMO_RLCA'''
    # {
    # 		write_byte(0x07);
    # 	}

def p_mnemo_rotate_2(p):
    '''mnemo_rotate : MNEMO_RLA'''
    # {
    # 		write_byte(0x17);
    # 	}

def p_mnemo_rotate_3(p):
    '''mnemo_rotate : MNEMO_RRCA'''
    # {
    # 		write_byte(0x0f);
    # 	}

def p_mnemo_rotate_4(p):
    '''mnemo_rotate : MNEMO_RRA'''
    # {
    # 		write_byte(0x1f);
    # 	}

def p_mnemo_rotate_5(p):
    '''mnemo_rotate : MNEMO_RLC REGISTER'''
    # {
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 	}

def p_mnemo_rotate_6(p):
    '''mnemo_rotate : MNEMO_RLC REGISTER_IND_HL'''
    # {
    # 		write_byte(0xcb);
    # 		write_byte(0x06);
    # 	}

def p_mnemo_rotate_7(p):
    '''mnemo_rotate : MNEMO_RLC rel_IX ',' REGISTER'''
    # {
    # 		if ($4 == 6)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte($4);
    # 	}

def p_mnemo_rotate_8(p):
    '''mnemo_rotate : MNEMO_RLC rel_IY ',' REGISTER'''
    # {
    # 		if ($4 == 6)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte($4);
    # 	}

def p_mnemo_rotate_9(p):
    '''mnemo_rotate : MNEMO_RLC rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte(0x06);
    # 	}

def p_mnemo_rotate_10(p):
    '''mnemo_rotate : MNEMO_RLC rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte(0x06);
    # 	}

def p_mnemo_rotate_11(p):
    '''mnemo_rotate : MNEMO_LD REGISTER ',' MNEMO_RLC rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($5);
    # 		write_byte($2);
    # 	}

def p_mnemo_rotate_12(p):
    '''mnemo_rotate : MNEMO_LD REGISTER ',' MNEMO_RLC rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($5);
    # 		write_byte($2);
    # 	}

def p_mnemo_rotate_13(p):
    '''mnemo_rotate : MNEMO_RL REGISTER'''
    # {
    # 		write_byte(0xcb);
    # 		write_byte(0x10 | $2);
    # 	}

def p_mnemo_rotate_14(p):
    '''mnemo_rotate : MNEMO_RL REGISTER_IND_HL'''
    # {
    # 		write_byte(0xcb);
    # 		write_byte(0x16);
    # 	}

def p_mnemo_rotate_15(p):
    '''mnemo_rotate : MNEMO_RL rel_IX ',' REGISTER'''
    # {
    # 		if ($4 == 6)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte($4 | 0x10);
    # 	}

def p_mnemo_rotate_16(p):
    '''mnemo_rotate : MNEMO_RL rel_IY ',' REGISTER'''
    # {
    # 		if ($4 == 6)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte($4 | 0x10);
    # 	}

def p_mnemo_rotate_17(p):
    '''mnemo_rotate : MNEMO_RL rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte(0x16);
    # 	}

def p_mnemo_rotate_18(p):
    '''mnemo_rotate : MNEMO_RL rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte(0x16);
    # 	}

def p_mnemo_rotate_19(p):
    '''mnemo_rotate : MNEMO_LD REGISTER ',' MNEMO_RL rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($5);
    # 		write_byte(0x10 | $2);
    # 	}

def p_mnemo_rotate_20(p):
    '''mnemo_rotate : MNEMO_LD REGISTER ',' MNEMO_RL rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($5);
    # 		write_byte(0x10 | $2);
    # 	}

def p_mnemo_rotate_21(p):
    '''mnemo_rotate : MNEMO_RRC REGISTER'''
    # {
    # 		write_byte(0xcb);
    # 		write_byte(0x08 | $2);
    # 	}

def p_mnemo_rotate_22(p):
    '''mnemo_rotate : MNEMO_RRC REGISTER_IND_HL'''
    # {
    # 		write_byte(0xcb);
    # 		write_byte(0x0e);
    # 	}

def p_mnemo_rotate_23(p):
    '''mnemo_rotate : MNEMO_RRC rel_IX ',' REGISTER'''
    # {
    # 		if ($4 == 6)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte($4 | 0x08);
    # 	}

def p_mnemo_rotate_24(p):
    '''mnemo_rotate : MNEMO_RRC rel_IY ',' REGISTER'''
    # {
    # 		if ($4 == 6)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte($4 | 0x08);
    # 	}

def p_mnemo_rotate_25(p):
    '''mnemo_rotate : MNEMO_RRC rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte(0x0e);
    # 	}

def p_mnemo_rotate_26(p):
    '''mnemo_rotate : MNEMO_RRC rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte(0x0e);
    # 	}

def p_mnemo_rotate_27(p):
    '''mnemo_rotate : MNEMO_LD REGISTER ',' MNEMO_RRC rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($5);
    # 		write_byte(0x08 | $2);
    # 	}

def p_mnemo_rotate_28(p):
    '''mnemo_rotate : MNEMO_LD REGISTER ',' MNEMO_RRC rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($5);
    # 		write_byte(0x08 | $2);
    # 	}

def p_mnemo_rotate_29(p):
    '''mnemo_rotate : MNEMO_RR REGISTER'''
    # {
    # 		write_byte(0xcb);
    # 		write_byte(0x18 | $2);
    # 	}

def p_mnemo_rotate_30(p):
    '''mnemo_rotate : MNEMO_RR REGISTER_IND_HL'''
    # {
    # 		write_byte(0xcb);
    # 		write_byte(0x1e);
    # 	}

def p_mnemo_rotate_31(p):
    '''mnemo_rotate : MNEMO_RR rel_IX ',' REGISTER'''
    # {
    # 		if ($4 == 6)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte($4 | 0x18);
    # 	}

def p_mnemo_rotate_32(p):
    '''mnemo_rotate : MNEMO_RR rel_IY ',' REGISTER'''
    # {
    # 		if ($4 == 6)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte($4 | 0x18);
    # 	}

def p_mnemo_rotate_33(p):
    '''mnemo_rotate : MNEMO_RR rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte(0x1e);
    # 	}

def p_mnemo_rotate_34(p):
    '''mnemo_rotate : MNEMO_RR rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte(0x1e);
    # 	}

def p_mnemo_rotate_35(p):
    '''mnemo_rotate : MNEMO_LD REGISTER ',' MNEMO_RR rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($5);
    # 		write_byte($2 | 0x18);
    # 	}

def p_mnemo_rotate_36(p):
    '''mnemo_rotate : MNEMO_LD REGISTER ',' MNEMO_RR rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($5);
    # 		write_byte($2 | 0x18);
    # 	}

def p_mnemo_rotate_37(p):
    '''mnemo_rotate : MNEMO_SLA REGISTER'''
    # {
    # 		write_byte(0xcb);
    # 		write_byte($2 | 0x20);
    # 	}

def p_mnemo_rotate_38(p):
    '''mnemo_rotate : MNEMO_SLA REGISTER_IND_HL'''
    # {
    # 		write_byte(0xcb);
    # 		write_byte(0x26);
    # 	}

def p_mnemo_rotate_39(p):
    '''mnemo_rotate : MNEMO_SLA rel_IX ',' REGISTER'''
    # {
    # 		if ($4 == 6)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte($4 | 0x20);
    # 	}

def p_mnemo_rotate_40(p):
    '''mnemo_rotate : MNEMO_SLA rel_IY ',' REGISTER'''
    # {
    # 		if ($4 == 6)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte($4 | 0x20);
    # 	}

def p_mnemo_rotate_41(p):
    '''mnemo_rotate : MNEMO_SLA rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte(0x26);
    # 	}

def p_mnemo_rotate_42(p):
    '''mnemo_rotate : MNEMO_SLA rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte(0x26);
    # 	}

def p_mnemo_rotate_43(p):
    '''mnemo_rotate : MNEMO_LD REGISTER ',' MNEMO_SLA rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($5);
    # 		write_byte($2 | 0x20);
    # 	}

def p_mnemo_rotate_44(p):
    '''mnemo_rotate : MNEMO_LD REGISTER ',' MNEMO_SLA rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($5);
    # 		write_byte($2 | 0x20);
    # 	}

def p_mnemo_rotate_45(p):
    '''mnemo_rotate : MNEMO_SLL REGISTER'''
    # {
    # 		write_byte(0xcb);
    # 		write_byte($2 | 0x30);
    # 	}

def p_mnemo_rotate_46(p):
    '''mnemo_rotate : MNEMO_SLL REGISTER_IND_HL'''
    # {
    # 		write_byte(0xcb);
    # 		write_byte(0x36);
    # 	}

def p_mnemo_rotate_47(p):
    '''mnemo_rotate : MNEMO_SLL rel_IX ',' REGISTER'''
    # {
    # 		if ($4 == 6)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte($4 | 0x30);
    # 	}

def p_mnemo_rotate_48(p):
    '''mnemo_rotate : MNEMO_SLL rel_IY ',' REGISTER'''
    # {
    # 		if ($4 == 6)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte($4 | 0x30);
    # 	}

def p_mnemo_rotate_49(p):
    '''mnemo_rotate : MNEMO_SLL rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte(0x36);
    # 	}

def p_mnemo_rotate_50(p):
    '''mnemo_rotate : MNEMO_SLL rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte(0x36);
    # 	}

def p_mnemo_rotate_51(p):
    '''mnemo_rotate : MNEMO_LD REGISTER ',' MNEMO_SLL rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($5);
    # 		write_byte($2 | 0x30);
    # 	}

def p_mnemo_rotate_52(p):
    '''mnemo_rotate : MNEMO_LD REGISTER ',' MNEMO_SLL rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($5);
    # 		write_byte($2 | 0x30);
    # 	}

def p_mnemo_rotate_53(p):
    '''mnemo_rotate : MNEMO_SRA REGISTER'''
    # {
    # 		write_byte(0xcb);
    # 		write_byte($2 | 0x28);
    # 	}

def p_mnemo_rotate_54(p):
    '''mnemo_rotate : MNEMO_SRA REGISTER_IND_HL'''
    # {
    # 		write_byte(0xcb);
    # 		write_byte(0x2e);
    # 	}

def p_mnemo_rotate_55(p):
    '''mnemo_rotate : MNEMO_SRA rel_IX ',' REGISTER'''
    # {
    # 		if ($4 == 6)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte($4 | 0x28);
    # 	}

def p_mnemo_rotate_56(p):
    '''mnemo_rotate : MNEMO_SRA rel_IY ',' REGISTER'''
    # {
    # 		if ($4 == 6)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte($4 | 0x28);
    # 	}

def p_mnemo_rotate_57(p):
    '''mnemo_rotate : MNEMO_SRA rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte(0x2e);
    # 	}

def p_mnemo_rotate_58(p):
    '''mnemo_rotate : MNEMO_SRA rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte(0x2e);
    # 	}

def p_mnemo_rotate_59(p):
    '''mnemo_rotate : MNEMO_LD REGISTER ',' MNEMO_SRA rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($5);
    # 		write_byte($2 | 0x28);
    # 	}

def p_mnemo_rotate_60(p):
    '''mnemo_rotate : MNEMO_LD REGISTER ',' MNEMO_SRA rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($5);
    # 		write_byte($2 | 0x28);
    # 	}

def p_mnemo_rotate_61(p):
    '''mnemo_rotate : MNEMO_SRL REGISTER'''
    # {
    # 		write_byte(0xcb);
    # 		write_byte($2 | 0x38);
    # 	}

def p_mnemo_rotate_62(p):
    '''mnemo_rotate : MNEMO_SRL REGISTER_IND_HL'''
    # {
    # 		write_byte(0xcb);
    # 		write_byte(0x3e);
    # 	}

def p_mnemo_rotate_63(p):
    '''mnemo_rotate : MNEMO_SRL rel_IX ',' REGISTER'''
    # {
    # 		if ($4 == 6)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte($4 | 0x38);
    # 	}

def p_mnemo_rotate_64(p):
    '''mnemo_rotate : MNEMO_SRL rel_IY ',' REGISTER'''
    # {
    # 		if ($4 == 6)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte($4 | 0x38);
    # 	}

def p_mnemo_rotate_65(p):
    '''mnemo_rotate : MNEMO_SRL rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte(0x3e);
    # 	}

def p_mnemo_rotate_66(p):
    '''mnemo_rotate : MNEMO_SRL rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($2);
    # 		write_byte(0x3e);
    # 	}

def p_mnemo_rotate_67(p):
    '''mnemo_rotate : MNEMO_LD REGISTER ',' MNEMO_SRL rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($5);
    # 		write_byte($2 | 0x38);
    # 	}

def p_mnemo_rotate_68(p):
    '''mnemo_rotate : MNEMO_LD REGISTER ',' MNEMO_SRL rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($5);
    # 		write_byte($2 | 0x38);
    # 	}

def p_mnemo_rotate_69(p):
    '''mnemo_rotate : MNEMO_RLD'''
    # {
    # 		write_byte(0xed);
    # 		write_byte(0x6f);
    # 	}

def p_mnemo_rotate_70(p):
    '''mnemo_rotate : MNEMO_RRD'''
    # {
    # 		write_byte(0xed);
    # 		write_byte(0x67);
    # 	}

def p_mnemo_bits_1(p):
    '''mnemo_bits : MNEMO_BIT value_3bits ',' REGISTER'''
    # {
    # 		write_byte(0xcb);
    # 		write_byte(0x40 | ($2 << 3) | ($4));
    # 	}

def p_mnemo_bits_2(p):
    '''mnemo_bits : MNEMO_BIT value_3bits ',' REGISTER_IND_HL'''
    # {
    # 		write_byte(0xcb);
    # 		write_byte(0x46 | ($2 << 3));
    # 	}

def p_mnemo_bits_3(p):
    '''mnemo_bits : MNEMO_BIT value_3bits ',' rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($4);
    # 		write_byte(0x46 | ($2 << 3));
    # 	}

def p_mnemo_bits_4(p):
    '''mnemo_bits : MNEMO_BIT value_3bits ',' rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($4);
    # 		write_byte(0x46 | ($2 << 3));
    # 	}

def p_mnemo_bits_5(p):
    '''mnemo_bits : MNEMO_SET value_3bits ',' REGISTER'''
    # {
    # 		write_byte(0xcb);
    # 		write_byte(0xc0 | ($2 << 3) | ($4));
    # 	}

def p_mnemo_bits_6(p):
    '''mnemo_bits : MNEMO_SET value_3bits ',' REGISTER_IND_HL'''
    # {
    # 		write_byte(0xcb);
    # 		write_byte(0xc6 | ($2 << 3));
    # 	}

def p_mnemo_bits_7(p):
    '''mnemo_bits : MNEMO_SET value_3bits ',' rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($4);
    # 		write_byte(0xc6 | ($2 << 3));
    # 	}

def p_mnemo_bits_8(p):
    '''mnemo_bits : MNEMO_SET value_3bits ',' rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($4);
    # 		write_byte(0xc6 | ($2 << 3));
    # 	}

def p_mnemo_bits_9(p):
    '''mnemo_bits : MNEMO_SET value_3bits ',' rel_IX ',' REGISTER'''
    # {
    # 		if ($6 == 6)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($4);
    # 		write_byte(0xc0 | ($2 << 3) | $6);
    # 	}

def p_mnemo_bits_10(p):
    '''mnemo_bits : MNEMO_SET value_3bits ',' rel_IY ',' REGISTER'''
    # {
    # 		if ($6 == 6)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($4);
    # 		write_byte(0xc0 | ($2 << 3) | $6);
    # 	}

def p_mnemo_bits_11(p):
    '''mnemo_bits : MNEMO_LD REGISTER ',' MNEMO_SET value_3bits ',' rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($7);
    # 		write_byte(0xc0 | ($5 << 3) | $2);
    # 	}

def p_mnemo_bits_12(p):
    '''mnemo_bits : MNEMO_LD REGISTER ',' MNEMO_SET value_3bits ',' rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($7);
    # 		write_byte(0xc0 | ($5 << 3) | $2);
    # 	}

def p_mnemo_bits_13(p):
    '''mnemo_bits : MNEMO_RES value_3bits ',' REGISTER'''
    # {
    # 		write_byte(0xcb);
    # 		write_byte(0x80 | ($2 << 3) | ($4));
    # 	}

def p_mnemo_bits_14(p):
    '''mnemo_bits : MNEMO_RES value_3bits ',' REGISTER_IND_HL'''
    # {
    # 		write_byte(0xcb);
    # 		write_byte(0x86 | ($2 << 3));
    # 	}

def p_mnemo_bits_15(p):
    '''mnemo_bits : MNEMO_RES value_3bits ',' rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($4);
    # 		write_byte(0x86 | ($2 << 3));
    # 	}

def p_mnemo_bits_16(p):
    '''mnemo_bits : MNEMO_RES value_3bits ',' rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($4);
    # 		write_byte(0x86 | ($2 << 3));
    # 	}

def p_mnemo_bits_17(p):
    '''mnemo_bits : MNEMO_RES value_3bits ',' rel_IX ',' REGISTER'''
    # {
    # 		if ($6 == 6)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($4);
    # 		write_byte(0x80 | ($2<<3) | $6);
    # 	}

def p_mnemo_bits_18(p):
    '''mnemo_bits : MNEMO_RES value_3bits ',' rel_IY ',' REGISTER'''
    # {
    # 		if ($6 == 6)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($4);
    # 		write_byte(0x80 | ($2 << 3) | $6);
    # 	}

def p_mnemo_bits_19(p):
    '''mnemo_bits : MNEMO_LD REGISTER ',' MNEMO_RES value_3bits ',' rel_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xcb);
    # 		write_byte($7);
    # 		write_byte(0x80 | ($5 << 3) | $2);
    # 	}

def p_mnemo_bits_20(p):
    '''mnemo_bits : MNEMO_LD REGISTER ',' MNEMO_RES value_3bits ',' rel_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xcb);
    # 		write_byte($7);
    # 		write_byte(0x80 | ($5 << 3) | $2);
    # 	}

def p_mnemo_io_1(p):
    '''mnemo_io : MNEMO_IN REGISTER ',' '[' value_8bits ']''''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		write_byte(0xdb);
    # 		write_byte($5);
    # 	}

def p_mnemo_io_2(p):
    '''mnemo_io : MNEMO_IN REGISTER ',' value_8bits'''
    # {
    # 		if ($2 != 7)
    # 		{
    # 			error_message(4, __FILE__, __LINE__);
    # 			exit(4);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xdb);
    # 		write_byte($4);
    # 	}

def p_mnemo_io_3(p):
    '''mnemo_io : MNEMO_IN REGISTER ',' '[' REGISTER ']''''
    # {
    # 		if ($5 != 1)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xed);
    # 		write_byte(0x40 | ($2 << 3));
    # 	}

def p_mnemo_io_4(p):
    '''mnemo_io : MNEMO_IN '[' REGISTER ']''''
    # {
    # 		if ($3 != 1)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xed);
    # 		write_byte(0x70);
    # 	}

def p_mnemo_io_5(p):
    '''mnemo_io : MNEMO_IN REGISTER_F ',' '[' REGISTER ']''''
    # {
    # 		if ($5 != 1)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xed);
    # 		write_byte(0x70);
    # 	}

def p_mnemo_io_6(p):
    '''mnemo_io : MNEMO_INI'''
    # {
    # 		write_byte(0xed);
    # 		write_byte(0xa2);
    # 	}

def p_mnemo_io_7(p):
    '''mnemo_io : MNEMO_INIR'''
    # {
    # 		write_byte(0xed);
    # 		write_byte(0xb2);
    # 	}

def p_mnemo_io_8(p):
    '''mnemo_io : MNEMO_IND'''
    # {
    # 		write_byte(0xed);
    # 		write_byte(0xaa);
    # 	}

def p_mnemo_io_9(p):
    '''mnemo_io : MNEMO_INDR'''
    # {
    # 		write_byte(0xed);
    # 		write_byte(0xba);
    # 	}

def p_mnemo_io_10(p):
    '''mnemo_io : MNEMO_OUT '[' value_8bits ']' ',' REGISTER'''
    # {
    # 		if ($6 != 7)
    # 		{
    # 			error_message(5, __FILE__, __LINE__);
    # 			exit(5);
    # 		}
    # 
    # 		write_byte(0xd3);
    # 		write_byte($3);
    # 	}

def p_mnemo_io_11(p):
    '''mnemo_io : MNEMO_OUT value_8bits ',' REGISTER'''
    # {
    # 		if ($4 != 7)
    # 		{
    # 			error_message(5, __FILE__, __LINE__);
    # 			exit(5);
    # 		}
    # 
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xd3);
    # 		write_byte($2);
    # 	}

def p_mnemo_io_12(p):
    '''mnemo_io : MNEMO_OUT '[' REGISTER ']' ',' REGISTER'''
    # {
    # 		if ($3 != 1)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xed);
    # 		write_byte(0x41 | ($6 << 3));
    # 	}

def p_mnemo_io_13(p):
    '''mnemo_io : MNEMO_OUT '[' REGISTER ']' ',' value_8bits'''
    # {
    # 		if ($3 != 1)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		if ($6 != 0)
    # 		{
    # 			error_message(6, __FILE__, __LINE__);
    # 			exit(6);
    # 		}
    # 
    # 		write_byte(0xed);
    # 		write_byte(0x71);
    # 	}

def p_mnemo_io_14(p):
    '''mnemo_io : MNEMO_OUTI'''
    # {
    # 		write_byte(0xed);
    # 		write_byte(0xa3);
    # 	}

def p_mnemo_io_15(p):
    '''mnemo_io : MNEMO_OTIR'''
    # {	write_byte(0xed);
    # 		write_byte(0xb3);
    # 	}

def p_mnemo_io_16(p):
    '''mnemo_io : MNEMO_OUTD'''
    # {
    # 		write_byte(0xed);
    # 		write_byte(0xab);
    # 	}

def p_mnemo_io_17(p):
    '''mnemo_io : MNEMO_OTDR'''
    # {
    # 		write_byte(0xed);
    # 		write_byte(0xbb);
    # 	}

def p_mnemo_io_18(p):
    '''mnemo_io : MNEMO_IN '[' value_8bits ']''''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xdb);
    # 		write_byte($3);
    # 	}

def p_mnemo_io_19(p):
    '''mnemo_io : MNEMO_IN value_8bits'''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xdb);
    # 		write_byte($2);
    # 	}

def p_mnemo_io_20(p):
    '''mnemo_io : MNEMO_OUT '[' value_8bits ']''''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xd3);
    # 		write_byte($3);
    # 	}

def p_mnemo_io_21(p):
    '''mnemo_io : MNEMO_OUT value_8bits'''
    # {
    # 		if (zilog)
    # 		{
    # 			warning_message(5, pass, source, lines, &warnings);
    # 		}
    # 
    # 		write_byte(0xd3);
    # 		write_byte($2);
    # 	}

def p_mnemo_jump_1(p):
    '''mnemo_jump : MNEMO_JP value_16bits'''
    # {
    # 		write_byte(0xc3);
    # 		write_word($2);
    # 	}

def p_mnemo_jump_2(p):
    '''mnemo_jump : MNEMO_JP CONDITION ',' value_16bits'''
    # {
    # 		write_byte(0xc2 | ($2 << 3));
    # 		write_word($4);
    # 	}

def p_mnemo_jump_3(p):
    '''mnemo_jump : MNEMO_JP REGISTER ',' value_16bits'''
    # {
    # 		if ($2 != 1)
    # 		{
    # 			error_message(7, __FILE__, __LINE__);
    # 			exit(7);
    # 		}
    # 
    # 		write_byte(0xda);
    # 		write_word($4);
    # 	}

def p_mnemo_jump_4(p):
    '''mnemo_jump : MNEMO_JR value_16bits'''
    # {
    # 		write_byte(0x18);
    # 		conditional_jump($2);
    # 	}

def p_mnemo_jump_5(p):
    '''mnemo_jump : MNEMO_JR REGISTER ',' value_16bits'''
    # {
    # 		if ($2 != 1)
    # 		{
    # 			error_message(7, __FILE__, __LINE__);
    # 			exit(7);
    # 		}
    # 
    # 		write_byte(0x38);
    # 		conditional_jump($4);
    # 	}

def p_mnemo_jump_6(p):
    '''mnemo_jump : MNEMO_JR CONDITION ',' value_16bits'''
    # {
    # 		if ($2 == 2)
    # 			write_byte(0x30);
    # 		else
    # 			if ($2 == 1)
    # 				write_byte(0x28);
    # 			else
    # 				if ($2 == 0)
    # 					write_byte(0x20);
    # 				else
    # 				{
    # 					error_message(9, __FILE__, __LINE__);
    # 					exit(9);
    # 				}
    # 
    # 		conditional_jump($4);
    # 	}

def p_mnemo_jump_7(p):
    '''mnemo_jump : MNEMO_JP REGISTER_PAR'''
    # {
    # 		if ($2 != 2)
    # 		{
    # 			error_message(2, __FILE__, __LINE__);
    # 			exit(2);
    # 		}
    # 
    # 		write_byte(0xe9);
    # 	}

def p_mnemo_jump_8(p):
    '''mnemo_jump : MNEMO_JP REGISTER_IND_HL'''
    # {
    # 		write_byte(0xe9);
    # 	}

def p_mnemo_jump_9(p):
    '''mnemo_jump : MNEMO_JP REGISTER_16_IX'''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xe9);
    # 	}

def p_mnemo_jump_10(p):
    '''mnemo_jump : MNEMO_JP REGISTER_16_IY'''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xe9);
    # 	}

def p_mnemo_jump_11(p):
    '''mnemo_jump : MNEMO_JP '[' REGISTER_16_IX ']''''
    # {
    # 		write_byte(0xdd);
    # 		write_byte(0xe9);
    # 	}

def p_mnemo_jump_12(p):
    '''mnemo_jump : MNEMO_JP '[' REGISTER_16_IY ']''''
    # {
    # 		write_byte(0xfd);
    # 		write_byte(0xe9);
    # 	}

def p_mnemo_jump_13(p):
    '''mnemo_jump : MNEMO_DJNZ value_16bits'''
    # {
    # 		write_byte(0x10);
    # 		conditional_jump($2);
    # 	}

def p_mnemo_call_1(p):
    '''mnemo_call : MNEMO_CALL value_16bits'''
    # {
    # 		write_byte(0xcd);
    # 		write_word($2);
    # 	}

def p_mnemo_call_2(p):
    '''mnemo_call : MNEMO_CALL CONDITION ',' value_16bits'''
    # {
    # 		write_byte(0xc4 | ($2 << 3));
    # 		write_word($4);
    # 	}

def p_mnemo_call_3(p):
    '''mnemo_call : MNEMO_CALL REGISTER ',' value_16bits'''
    # {
    # 		if ($2 != 1)
    # 		{
    # 			error_message(7, __FILE__, __LINE__);
    # 			exit(7);
    # 		}
    # 
    # 		write_byte(0xdc);
    # 		write_word($4);
    # 	}

def p_mnemo_call_4(p):
    '''mnemo_call : MNEMO_RET'''
    # {
    # 		write_byte(0xc9);
    # 	}

def p_mnemo_call_5(p):
    '''mnemo_call : MNEMO_RET CONDITION'''
    # {
    # 		write_byte(0xc0 | ($2 << 3));
    # 	}

def p_mnemo_call_6(p):
    '''mnemo_call : MNEMO_RET REGISTER'''
    # {
    # 		if ($2 != 1)
    # 		{
    # 			error_message(7, __FILE__, __LINE__);
    # 			exit(7);
    # 		}
    # 
    # 		write_byte(0xd8);
    # 	}

def p_mnemo_call_7(p):
    '''mnemo_call : MNEMO_RETI'''
    # {
    # 		write_byte(0xed);
    # 		write_byte(0x4d);
    # 	}

def p_mnemo_call_8(p):
    '''mnemo_call : MNEMO_RETN'''
    # {
    # 		write_byte(0xed);
    # 		write_byte(0x45);
    # 	}

def p_mnemo_call_9(p):
    '''mnemo_call : MNEMO_RST value_8bits'''
    # {
    # 		if (((int)($2) % 8 != 0) || ((int)($2) / 8 > 7) || ((int)($2) / 8 < 0))
    # 		{
    # 			error_message(10, __FILE__, __LINE__);
    # 			exit(10);
    # 		}
    # 
    # 		write_byte(0xc7 | (($2 / 8) << 3));
    # 	}

def p_value_1(p):
    '''value : NUMBER'''
    # {
    # 		$$ = $1;
    # 	}

def p_value_2(p):
    '''value : IDENTIFICATOR'''
    # {
    # 		$$ = read_label($1);
    # 	}

def p_value_3(p):
    '''value : LOCAL_IDENTIFICATOR'''
    # {
    # 		$$ = read_local($1);
    # 	}

def p_value_4(p):
    '''value : '-' value %prec NEGATIVE'''
    # {
    # 		$$ = -((int)($2));
    # 	}

def p_value_5(p):
    '''value : value OP_EQUAL value'''
    # {
    # 		$$ = ($1 == $3);
    # 	}

def p_value_6(p):
    '''value : value OP_MINOR_EQUAL value'''
    # {
    # 		$$ = ($1 <= $3);
    # 	}

def p_value_7(p):
    '''value : value OP_MINOR value'''
    # {
    # 		$$ = ($1 < $3);
    # 	}

def p_value_8(p):
    '''value : value OP_MAJOR_EQUAL value'''
    # {
    # 		$$ = ($1 >= $3);
    # 	}

def p_value_9(p):
    '''value : value OP_MAJOR value'''
    # {
    # 		$$ = ($1 > $3);
    # 	}

def p_value_10(p):
    '''value : value OP_NON_EQUAL value'''
    # {
    # 		$$ = ($1 != $3);
    # 	}

def p_value_11(p):
    '''value : value OP_OR_LOG value'''
    # {
    # 		$$ = ($1 || $3);
    # 	}

def p_value_12(p):
    '''value : value OP_AND_LOG value'''
    # {
    # 		$$ = ($1 && $3);
    # 	}

def p_value_13(p):
    '''value : value '+' value'''
    # {
    # 		$$ = $1 + $3;
    # 	}

def p_value_14(p):
    '''value : value '-' value'''
    # {
    # 		$$ = $1 - $3;
    # 	}

def p_value_15(p):
    '''value : value '*' value'''
    # {
    # 		$$ = $1 * $3;
    # 	}

def p_value_16(p):
    '''value : value '/' value'''
    # {
    # 		if (!$3)
    # 		{
    # 			error_message(1, __FILE__, __LINE__);
    # 			exit(1);
    # 		}
    # 		else
    # 			$$ = $1 / $3;
    # 	}

def p_value_17(p):
    '''value : value '%' value'''
    # {
    # 		if (!$3)
    # 		{
    # 			error_message(1, __FILE__, __LINE__);
    # 			exit(1);
    # 		}
    # 		else $$ = $1 % $3;
    # 	}

def p_value_18(p):
    '''value : '(' value ')''''
    # {
    # 		$$ = $2;
    # 	}

def p_value_19(p):
    '''value : '~' value %prec NEGATION'''
    # {
    # 		$$ = ~$2;
    # 	}

def p_value_20(p):
    '''value : '!' value %prec OP_NEG_LOG'''
    # {
    # 		$$ = !$2;
    # 	}

def p_value_21(p):
    '''value : value '&' value'''
    # {
    # 		$$ = $1 & $3;
    # 	}

def p_value_22(p):
    '''value : value OP_OR value'''
    # {
    # 		$$ = $1 | $3;
    # 	}

def p_value_23(p):
    '''value : value OP_XOR value'''
    # {
    # 		$$ = $1 ^ $3;
    # 	}

def p_value_24(p):
    '''value : value SHIFT_L value'''
    # {
    # 		$$ = $1 << $3;
    # 	}

def p_value_25(p):
    '''value : value SHIFT_R value'''
    # {
    # 		$$ = $1 >> $3;
    # 	}

def p_value_26(p):
    '''value : PSEUDO_RANDOM '(' value ')''''
    # {
    # 		for (; ($$ = rand() & 0xff) >= $3;)
    # 			;
    # 	}

def p_value_27(p):
    '''value : PSEUDO_INT '(' value_real ')''''
    # {
    # 		$$ = (int)$3;
    # 	}

def p_value_28(p):
    '''value : PSEUDO_FIX '(' value_real ')''''
    # {
    # 		$$ = (int)($3 * 256);
    # 	}

def p_value_29(p):
    '''value : PSEUDO_FIXMUL '(' value ',' value ')''''
    # {
    # 		$$ = (int)((((float)$3 / 256) * ((float)$5 / 256)) * 256);
    # 	}

def p_value_30(p):
    '''value : PSEUDO_FIXDIV '(' value ',' value ')''''
    # {
    # 		$$ = (int)((((float)$3 / 256) / ((float)$5 / 256)) * 256);
    # 	}

def p_value_real_1(p):
    '''value_real : REAL'''
    # {
    # 		$$ = $1;
    # 	}

def p_value_real_2(p):
    '''value_real : '-' value_real'''
    # {
    # 		$$ = -$2;
    # 	}

def p_value_real_3(p):
    '''value_real : value_real '+' value_real'''
    # {
    # 		$$ = $1 + $3;
    # 	}

def p_value_real_4(p):
    '''value_real : value_real '-' value_real'''
    # {
    # 		$$ = $1 - $3;
    # 	}

def p_value_real_5(p):
    '''value_real : value_real '*' value_real'''
    # {
    # 		$$ = $1 * $3;
    # 	}

def p_value_real_6(p):
    '''value_real : value_real '/' value_real'''
    # {
    # 		if (!$3)
    # 		{
    # 			error_message(1, __FILE__, __LINE__);
    # 			exit(1);
    # 		}
    # 		else
    # 			$$ = $1 / $3;
    # 	}

def p_value_real_7(p):
    '''value_real : value '+' value_real'''
    # {
    # 		$$ = (double)$1 + $3;
    # 	}

def p_value_real_8(p):
    '''value_real : value '-' value_real'''
    # {
    # 		$$ = (double)$1 - $3;
    # 	}

def p_value_real_9(p):
    '''value_real : value '*' value_real'''
    # {
    # 		$$ = (double)$1 * $3;
    # 	}

def p_value_real_10(p):
    '''value_real : value '/' value_real'''
    # {
    # 		if ($3 < 1e-6)
    # 		{
    # 			error_message(1, __FILE__, __LINE__);
    # 			exit(1);
    # 		}
    # 		else
    # 			$$ = (double)$1 / $3;
    # 	}

def p_value_real_11(p):
    '''value_real : value_real '+' value'''
    # {
    # 		$$ = $1 + (double)$3;
    # 	}

def p_value_real_12(p):
    '''value_real : value_real '-' value'''
    # {
    # 		$$ = $1 - (double)$3;
    # 	}

def p_value_real_13(p):
    '''value_real : value_real '*' value'''
    # {
    # 		$$ = $1 * (double)$3;
    # 	}

def p_value_real_14(p):
    '''value_real : value_real '/' value'''
    # {
    # 		if (!$3)
    # 		{
    # 			error_message(1, __FILE__, __LINE__);
    # 			exit(1);
    # 		}
    # 		else
    # 			$$ = $1 / (double)$3;
    # 	}

def p_value_real_15(p):
    '''value_real : PSEUDO_SIN '(' value_real ')''''
    # {
    # 		$$ = sin($3);
    # 	}

def p_value_real_16(p):
    '''value_real : PSEUDO_COS '(' value_real ')''''
    # {
    # 		$$ = cos($3);
    # 	}

def p_value_real_17(p):
    '''value_real : PSEUDO_TAN '(' value_real ')''''
    # {
    # 		$$ = tan($3);
    # 	}

def p_value_real_18(p):
    '''value_real : PSEUDO_SQR '(' value_real ')''''
    # {
    # 		$$ = $3 * $3;
    # 	}

def p_value_real_19(p):
    '''value_real : PSEUDO_SQRT '(' value_real ')''''
    # {
    # 		$$ = sqrt($3);
    # 	}

def p_value_real_20(p):
    '''value_real : PSEUDO_PI'''
    # {
    # 		$$ = asin(1) * 2;
    # 	}

def p_value_real_21(p):
    '''value_real : PSEUDO_ABS '(' value_real ')''''
    # {
    # 		$$ = (($3) < 0) ? -($3) : ($3);
    # 	}

def p_value_real_22(p):
    '''value_real : PSEUDO_ACOS '(' value_real ')''''
    # {
    # 		$$ = acos($3);
    # 	}

def p_value_real_23(p):
    '''value_real : PSEUDO_ASIN '(' value_real ')''''
    # {
    # 		$$ = asin($3);
    # 	}

def p_value_real_24(p):
    '''value_real : PSEUDO_ATAN '(' value_real ')''''
    # {
    # 		$$ = atan($3);
    # 	}

def p_value_real_25(p):
    '''value_real : PSEUDO_EXP '(' value_real ')''''
    # {
    # 		$$ = exp($3);
    # 	}

def p_value_real_26(p):
    '''value_real : PSEUDO_LOG '(' value_real ')''''
    # {
    # 		$$ = log10($3);
    # 	}

def p_value_real_27(p):
    '''value_real : PSEUDO_LN '(' value_real ')''''
    # {
    # 		$$ = log($3);
    # 	}

def p_value_real_28(p):
    '''value_real : PSEUDO_POW '(' value_real ',' value_real ')''''
    # {
    # 		$$ = pow($3, $5);
    # 	}

def p_value_real_29(p):
    '''value_real : '(' value_real ')''''
    # {
    # 		$$ = $2;
    # 	}

def p_value_3bits_1(p):
    '''value_3bits : value'''
    # {
    # 		if (((int)$1 < 0) || ((int)$1 > 7))
    # 		{
    # 			warning_message(3, pass, source, lines, &warnings);
    # 		}
    # 
    # 		$$ = $1 & 0x07;
    # 	}

def p_value_8bits_1(p):
    '''value_8bits : value'''
    # {
    # 		if (((int)$1 > 255) || ((int) $1 < -128))
    # 		{
    # 			warning_message(2, pass, source, lines, &warnings);
    # 		}
    # 
    # 		$$ = $1 & 0xff;
    # 	}

def p_value_16bits_1(p):
    '''value_16bits : value'''
    # {
    # 		if (((int)$1 > 65535) || ((int)$1 < -32768))
    # 		{
    # 			warning_message(1, pass, source, lines, &warnings);
    # 		}
    # 
    # 		$$ = $1 & 0xffff;
    # 	}

def p_listing_8bits_1(p):
    '''listing_8bits : value_8bits'''
    # {
    # 		write_byte($1);
    # 	}

def p_listing_8bits_2(p):
    '''listing_8bits : TEXT'''
    # {
    # 		write_text($1);
    # 	}

def p_listing_8bits_3(p):
    '''listing_8bits : listing_8bits ',' value_8bits'''
    # {
    # 		write_byte($3);
    # 	}

def p_listing_8bits_4(p):
    '''listing_8bits : listing_8bits ',' TEXT'''
    # {
    # 		write_text($3);
    # 	}

def p_listing_16bits_1(p):
    '''listing_16bits : value_16bits'''
    # {
    # 		write_word($1);
    # 	}

def p_listing_16bits_2(p):
    '''listing_16bits : TEXT'''
    # {
    # 		write_text($1);
    # 	}

def p_listing_16bits_3(p):
    '''listing_16bits : listing_16bits ',' value_16bits'''
    # {
    # 		write_word($3);
    # 	}

def p_listing_16bits_4(p):
    '''listing_16bits : listing_16bits ',' TEXT'''
    # {
    # 		write_text($3);
    # 	}

# -------------- RULES END ----------------
# 
# 
# void yyerror(const char *s)
# {
# 	printf("yyerror: %s\n", s);
# 	error_message(0, __FILE__, __LINE__);
# 	exit(0);
# }

if __name__ == '__main__':
    from ply import *
    yacc.yacc()

