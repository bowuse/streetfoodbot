import sqlite3

db_file = './places.db'


def add_user(id, username):
	with sqlite3.connect(db_file) as db:
		try:
			c = db.cursor()
			c.execute("""INSERT INTO users (id, username)
				VALUES (?,?)""", (id, username))
			db.commit()
		except Exception as e:
			print(f"Exception adding user, {e}")
			db.rollback()


def add_descr(id, name, tag, price_tag, descr, mark, obzor_link, img_link):
	with sqlite3.connect(db_file) as db:
		try:
			c = db.cursor()
			c.execute("""INSERT INTO place_descr (
				id, name, tag, price_tag, descr, mark, obzor_link, img_link
			) VALUES (?,?,?,?,?,?,?,?)
			""",(id, name, tag, price_tag, descr, mark, obzor_link, img_link))
			db.commit()
			return True
		except Exception as e:
			print(e)
			db.rollback()
			return False


def add_location(id, address, lat, long, map_link):
	with sqlite3.connect(db_file) as db:
		try:
			c = db.cursor()
			c.execute("""INSERT INTO place_location (id, address, lat, long, map_link) 
				VALUES (?,?,?,?,?)""",
				(id, address, lat, long, map_link))
			db.commit()
			return True
		except Exception as e:
			print(e)
			db.rollback()
			return False


def get_name(id):
	with sqlite3.connect(db_file) as db:
		try:
			c = db.cursor()
			c.execute("""SELECT name FROM place_descr WHERE id=?""",(id,))
			name = c.fetchone()
			return name[0]
		except Exception as e:
			print(f"get_name Exception: {e}")


def get_tag(id):
	with sqlite3.connect(db_file) as db:
		try:
			c = db.cursor()
			c.execute("""SELECT tag FROM place_descr WHERE id=?""",(id,))
			tag = c.fetchone()
			return tag[0]
		except Exception as e:
			print(f"get_tag Exception: {e}")


def get_price_tag(id):
	with sqlite3.connect(db_file) as db:
		try:
			c = db.cursor()
			c.execute("""SELECT price_tag FROM place_descr WHERE id=?""",(id,))
			price_tag = c.fetchone()
			return price_tag[0]
		except Exception as e:
			print(f"get_price_tag Exception: {e}")


def get_address(id):
	with sqlite3.connect(db_file) as db:
		try:
			c = db.cursor()
			c.execute("""SELECT address FROM place_location WHERE id=?""",(id,))
			adrr = c.fetchall()
			adrr = [i[0] for i in adrr]
			return adrr
		except Exception as e:
			print(f"get_address Exception: {e}")


def get_lat(id):
	with sqlite3.connect(db_file) as db:
		try:
			c = db.cursor()
			c.execute("""SELECT lat FROM place_location WHERE id=?""",(id,))
			lat = c.fetchall()
			lat = [i[0] for i in lat]
			return lat
		except Exception as e:
			print(f"get_lat Exception: {e}")


def get_long(id):
	with sqlite3.connect(db_file) as db:
		try:
			c = db.cursor()
			c.execute("""SELECT long FROM place_location WHERE id=?""",(id,))
			long = c.fetchall()
			long = [i[0] for i in long]
			return long
		except Exception as e:
			print(f"get_long Exception: {e}")


def get_descr(id):
	with sqlite3.connect(db_file) as db:
		try:
			c = db.cursor()
			c.execute("""SELECT descr FROM place_descr WHERE id=?""",(id,))
			descr = c.fetchone()
			return descr[0]
		except Exception as e:
			print(f"get_descr Exception: {e}")


def get_mark(id):
	with sqlite3.connect(db_file) as db:
		try:
			c = db.cursor()
			c.execute("""SELECT mark FROM place_descr WHERE id=?""",(id,))
			mark = c.fetchone()
			return mark[0]
		except Exception as e:
			print(f"get_mark Exception: {e}")


def get_obzor_link(id):
	with sqlite3.connect(db_file) as db:
		try:
			c = db.cursor()
			c.execute("""SELECT obzor_link FROM place_descr WHERE id=?""",(id,))
			obzor_link = c.fetchone()
			return obzor_link[0]
		except Exception as e:
			print(f"get_obzor_link Exception: {e}")


def get_img_link(id):
	with sqlite3.connect(db_file) as db:
		try:
			c = db.cursor()
			c.execute("""SELECT img_link FROM place_descr WHERE id=?""",(id,))
			img_link = c.fetchone()
			return img_link[0]
		except Exception as e:
			print(f"get_img_link Exception: {e}")


def get_map_link(id):
	with sqlite3.connect(db_file) as db:
		try:
			c = db.cursor()
			c.execute("""SELECT map_link FROM place_location WHERE id=?""",(id,))
			map_link = c.fetchall()
			map_link = [i[0] for i in map_link]
			return map_link
		except Exception as e:
			print(f"get_map_link Exception: {e}")


def test():
	print(get_map_link('1'))
	print(get_address('29'))
	
				



if __name__ == "__main__":
	pass
	#test()
